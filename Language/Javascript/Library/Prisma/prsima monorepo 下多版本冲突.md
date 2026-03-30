# prsima monorepo 下多版本冲突

今天吾辈遇到了这个错误，`TypeError: undefined is not an object (evaluating 't.graph')`，完整报错在底下，属实看不出任何猫腻，完完全全卡住了。

之后想到很多问题啊，比如，两个schema会不会导致冲突啊，然而在重新`bun install`，也解决不了问题的情况下思路卡住了，不过想到了bun.lock没删，再加上版本的确不匹配，

```sh
YOUR_WORKSPACE_DIR\package\auth $ bunx prisma --version  
Loaded Prisma config from prisma.config.ts.

Prisma schema loaded from prisma\schema.prisma.
prisma               : 7.3.0
@prisma/client       : 7.4.2
Operating System     : win32
Architecture         : x64
Node.js              : v25.6.0
TypeScript           : 5.9.2
Query Compiler       : enabled
PSL                  : @prisma/prisma-schema-wasm 7.5.0-10.94a226be1cf2967af2541cca5529f0f7ba866919
Schema Engine        : schema-engine-cli 94a226be1cf2967af2541cca5529f0f7ba866919 (at ..\..\node_modules\.bun\@prisma+engines@7.4.2\node_modules\@prisma\engines\schema-engine-windows.exe)
Default Engines Hash : 94a226be1cf2967af2541cca5529f0f7ba866919
Studio               : 0.13.1
```

我也不能确定，但是当时大概就是这个输出。

所幸更新了一下版本，最后确定了问题，得到的教训就是prisma一定要锁定版本，最好不要写"^7.4.2"，直接写"7.4.2"，不过吾辈目前还是写了^就是了，只不过因为有两个数据库，所以更新的话需要改8个地方（每个包四个），不知道怎么解决会比较好呢？


## 完整报错

```
6 | `)}};var Vu={red:be,gray:lt,dim:it,bold:G,underline:ot,highlightSource:e=>e.highlight()},qu={red:e=>e,gray:e=>e,dim:e=>e,bold:e=>e,underline:e=>e,highlightSource:e=>e};function ju({message:e,originalMethod:t,isPanic:r,callArguments:n}){return{functionName:`prisma.${t}()`,message:e,isPanic:r??!1,callArguments:n}}function Uu({callsite:e,message:t,originalMethod:r,isPanic:n,callArguments:i},o){let s=ju({message:t,originalMethod:r,isPanic:n,callArguments:i});if(!e||typeof window<"u"||process.env.NODE_ENV==="production")return s;let a=e.getLocation();if(!a||!a.lineNumber||!a.columnNumber)return s;let l=Math.max(1,a.lineNumber-3),u=Xt.read(a.fileName)?.slice(l,a.lineNumber),c=u?.lineAt(a.lineNumber);if(u&&c){let p=Qu(c),d=Bu(c);if(!d)return s;s.functionName=`${d.code})`,s.location=a,n||(u=u.mapLineAt(a.lineNumber,h=>h.slice(0,d.openingBraceIndex))),u=o.highlightSource(u);let f=String(u.lastLineNumber).length;if(s.contextLines=u.mapLines((h,x)=>o.gray(String(x).padStart(f))+" "+h).mapLines(h=>o.dim(h)).prependSymbol | ... truncated 
 7 | `)}function Hu(e){let t=[e.fileName];return e.lineNumber&&t.push(String(e.lineNumber)),e.columnNumber&&t.push(String(e.columnNumber)),t.join(":")}function er(e){let t=e.showColors?Vu:qu,r;return r=Uu(e,t),Ju(r,t)}var so=U(cn());function to(e,t,r){let n=ro(e),i=Gu(n),o=Wu(i);o?tr(o,t,r):t.addErrorMessage(()=>"Unknown error")}function ro(e){return e.errors.flatMap(t=>t.kind==="Union"?ro(t):[t])}function Gu(e){let t=new Map,r=[];for(let n of e){if(n.kind!=="InvalidArgumentType"){r.push(n);continue}let i=`${n.selectionPath.join(".")}:${n.argumentPath.join(".")}`,o=t.get(i);o?t.set(i,{...n,argument:{...n.argument,typeNames:zu(o.argument.typeNames,n.argument.typeNames)}}):t.set(i,n)}return r.push(...t.values()),r}function zu(e,t){return[...new Set(e.concat(t))]}function Wu(e){return ln(e,(t,r)=>{let n=Xi(t),i=Xi(r);return n!==i?n-i:eo(t)-eo(r)})}function Xi(e){let t=0;return Array.isArray(e.selectionPath)&&(t+=e.selectionPath.length),Array.isArray(e.argumentPath)&&(t+=e.argumentPath.length),t}function eo(e){switch( | ... truncated 
 8 | `)}getCurrentLineLength(){return this.currentLine.length}indentedCurrentLine(){let t=this.currentLine.padStart(this.currentLine.length+2*this.currentIndent);return this.marginSymbol?this.marginSymbol+t.slice(1):t}};no();var rr=class{constructor(t){this.value=t}write(t){t.write(this.value)}markAsError(){this.value.markAsError()}};var nr=e=>e,ir={bold:nr,red:nr,green:nr,dim:nr,enabled:!1},oo={bold:G,red:be,green:st,dim:it,enabled:!0},Le={write(e){e.writeLine(",")}};var Y=class{constructor(t){this.contents=t}isUnderlined=!1;color=t=>t;underline(){return this.isUnderlined=!0,this}setColor(t){return this.color=t,this}write(t){let r=t.getCurrentLineLength();t.write(this.color(this.contents)),this.isUnderlined&&t.afterNextNewline(()=>{t.write(" ".repeat(r)).writeLine(this.color("~".repeat(this.contents.length)))})}};var pe=class{hasError=!1;markAsError(){return this.hasError=!0,this}};var $e=class extends pe{items=[];addItem(t){return this.items.push(new rr(t)),this}getField(t){return this.items[t]}getPrintWidth(){r | ... truncated 
 9 | Note that ${s.bold("include")} statements only accept relation fields.`,a})}function Yu(e,t,r){let n=t.arguments.getDeepSubSelectionValue(e.selectionPath)?.asObject();if(n){let i=n.getField("omit")?.value.asObject();if(i){Xu(e,t,i);return}if(n.hasField("select")){ec(e,t);return}}if(r?.[ce(e.outputType.name)]){tc(e,t);return}t.addErrorMessage(()=>`Unknown field at "${e.selectionPath.join(".")} selection"`)}function Xu(e,t,r){r.removeAllFields();for(let n of e.outputType.fields)r.addSuggestion(new q(n.name,"false"));t.addErrorMessage(n=>`The ${n.red("omit")} statement includes every field of the model ${n.bold(e.outputType.name)}. At least one field must be included in the result`)}function ec(e,t){let r=e.outputType,n=t.arguments.getDeepSelectionParent(e.selectionPath)?.value,i=n?.isEmpty()??!1;n&&(n.removeAllFields(),uo(n,r)),t.addErrorMessage(o=>i?`The ${o.red("`select`")} statement for type ${o.bold(r.name)} must not be empty. ${ht(o)}`:`The ${o.red("`select`")} statement for type ${o.bold(r.name)} needs ${ | ... truncated 
10 | `)}};function Ue(e){return new dn(go(e))}function go(e){let t=new Ve;for(let[r,n]of Object.entries(e)){let i=new sr(r,yo(n));t.addField(i)}return t}function yo(e){if(typeof e=="string")return new k(JSON.stringify(e));if(typeof e=="number"||typeof e=="boolean")return new k(String(e));if(typeof e=="bigint")return new k(`${e}n`);if(e===null)return new k("null");if(e===void 0)return new k("undefined");if(Fe(e))return new k(`new Prisma.Decimal("${e.toFixed()}")`);if(e instanceof Uint8Array)return Buffer.isBuffer(e)?new k(`Buffer.alloc(${e.byteLength})`):new k(`new Uint8Array(${e.byteLength})`);if(e instanceof Date){let t=Zt(e)?e.toISOString():"Invalid Date";return new k(`new Date("${t}")`)}return e instanceof fo.ObjectEnumValue?new k(`Prisma.${e._getName()}`):je(e)?new k(`prisma.${ce(e.modelName)}.$fields.${e.name}`):Array.isArray(e)?hc(e):typeof e=="object"?go(e):new k(Object.prototype.toString.call(e))}function hc(e){let t=new $e;for(let r of e)t.addItem(yo(r));return t}function ar(e,t){let r=t==="pretty"?oo:ir, | ... truncated 
11 | `);return t.reduce(function(r,n){var i=Dc(n)||Mc(n)||$c(n)||Uc(n)||qc(n);return i&&r.push(i),r},[])}var Oc=/^\s*at (.*?) ?\(((?:file|https?|blob|chrome-extension|native|eval|webpack|rsc|<anonymous>|\/|[a-z]:\\|\\\\).*?)(?::(\d+))?(?::(\d+))?\)?\s*$/i,Nc=/\((\S*)(?::(\d+))(?::(\d+))\)/;function Dc(e){var t=Oc.exec(e);if(!t)return null;var r=t[2]&&t[2].indexOf("native")===0,n=t[2]&&t[2].indexOf("eval")===0,i=Nc.exec(t[2]);return n&&i!=null&&(t[2]=i[1],t[3]=i[2],t[4]=i[3]),{file:r?null:t[2],methodName:t[1]||Tt,arguments:r?[t[2]]:[],lineNumber:t[3]?+t[3]:null,column:t[4]?+t[4]:null}}var Fc=/^\s*at (?:((?:\[object object\])?.+) )?\(?((?:file|ms-appx|https?|webpack|rsc|blob):.*?):(\d+)(?::(\d+))?\)?\s*$/i;function Mc(e){var t=Fc.exec(e);return t?{file:t[2],methodName:t[1]||Tt,arguments:[],lineNumber:+t[3],column:t[4]?+t[4]:null}:null}var _c=/^\s*(.*?)(?:\((.*?)\))?(?:^|@)((?:file|https?|blob|chrome|webpack|rsc|resource|\[native).*?|[^@]*bundle)(?::(\d+))?(?::(\d+))?\s*$/i,Lc=/(\S+) line (\d+)(?: > eval line \d+)* > | ... truncated 

TypeError: undefined is not an object (evaluating 't.graph')
 clientVersion: "7.3.0",

      at new ii (YOUR_WORKSPACE_DIR\node_modules\@prisma\client\runtime\client.js:11:56375)
      at Fa (YOUR_WORKSPACE_DIR\node_modules\@prisma\client\runtime\client.js:11:56244)
      at deserialize (YOUR_WORKSPACE_DIR\node_modules\@prisma\client\runtime\client.js:11:57817)
      at new jt (YOUR_WORKSPACE_DIR\node_modules\@prisma\client\runtime\client.js:57:17465)
      at ml (YOUR_WORKSPACE_DIR\node_modules\@prisma\client\runtime\client.js:58:6195)
      at new t (YOUR_WORKSPACE_DIR\node_modules\@prisma\client\runtime\client.js:75:71)
      at YOUR_WORKSPACE_DIR\package\server\prisma\client.ts:28:23
```