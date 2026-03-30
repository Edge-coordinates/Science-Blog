
有非常多种情况能够导致这该死的问题，以下稍作列举

## zustand selector

需要使用多个独立 selector。

下面的写法每次`render`都会返回一个新对象，在 React 19 的 useSyncExternalStore 下会触发你看到的 The result of getSnapshot should be cached，然后一路把整个树拖进无限更新，最后又表现成 InputBase 被动 effect 爆栈。

```typescript
const {
authSession,
capabilityLevel,
hasAuthSession,
needsOnboarding,
needsVerification,
status,
} = useAuthSessionStore(state => ({
authSession: state.authSession,
capabilityLevel: state.capabilityLevel,
hasAuthSession: state.hasAuthSession,
needsOnboarding: state.needsOnboarding,
needsVerification: state.needsVerification,
status: state.status,
}));
```
