#!/usr/bin/env node
// Usage: node fetch_lottie.js <project_dir> <spec>...
//   spec: noto:<codepoint>[:name]          -> Google Noto animated emoji (CC BY 4.0)
//         ua:<iconName>[:#hex][:name]       -> useAnimations (MIT), recolored stroke/fill
// Writes <project>/public/lottie/<name>.json and appends to <project>/CREDITS.md
const fs = require('fs'), path = require('path'), os = require('os'), {execSync} = require('child_process');
const [proj, ...specs] = process.argv.slice(2);
const out = path.join(proj, 'public', 'lottie'); fs.mkdirSync(out, {recursive: true});
const credits = path.join(proj, 'CREDITS.md');
if (!fs.existsSync(credits)) fs.writeFileSync(credits, '# Third-party asset credits\n\n');
const uaDir = path.join(os.tmpdir(), 'ua-pkg', 'package');
function ensureUA() {
  if (fs.existsSync(uaDir)) return;
  fs.mkdirSync(path.join(os.tmpdir(), 'ua-pkg'), {recursive: true});
  execSync('npm pack react-useanimations@3.1.1 -q && tar xzf react-useanimations-3.1.1.tgz', {cwd: path.join(os.tmpdir(), 'ua-pkg')});
}
function hex2rgb(h){h=h.replace('#','');return [0,2,4].map(i=>parseInt(h.slice(i,i+2),16)/255);}
function recolor(node, rgb){
  if (Array.isArray(node)) return node.forEach(n=>recolor(n,rgb));
  if (node && typeof node==='object'){
    if ((node.ty==='st'||node.ty==='fl') && node.c && node.c.a===0) node.c.k=[...rgb,1];
    Object.values(node).forEach(v=>recolor(v,rgb));
  }
}
(async()=>{
  for (const spec of specs){
    const p = spec.split(':');
    if (p[0]==='noto'){
      const name = p[2]||('noto_'+p[1]);
      const url = `https://fonts.gstatic.com/s/e/notoemoji/latest/${p[1]}/lottie.json`;
      const r = await fetch(url); if (!r.ok) throw new Error(url+' '+r.status);
      fs.writeFileSync(path.join(out, name+'.json'), await r.text());
      fs.appendFileSync(credits, `- ${name}.json: Noto Animated Emoji U+${p[1].toUpperCase()} by Google, CC BY 4.0 (https://googlefonts.github.io/noto-emoji-animation/) - ${url}\n`);
    } else if (p[0]==='ua'){
      ensureUA();
      const color = p[2]||'#ffffff', name = p[3]||('ua_'+p[1]);
      const data = JSON.parse(JSON.stringify(require(path.join(uaDir,'lib',p[1]+'.js')).default.animationData));
      recolor(data, hex2rgb(color));
      fs.writeFileSync(path.join(out, name+'.json'), JSON.stringify(data));
      fs.appendFileSync(credits, `- ${name}.json: useAnimations "${p[1]}" (react-useanimations 3.1.1), MIT License - https://useanimations.com\n`);
    } else throw new Error('bad spec '+spec);
    console.log('ok', spec);
  }
})().catch(e=>{console.error(e);process.exit(1);});
