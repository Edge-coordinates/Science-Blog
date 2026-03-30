> 原文地址 [steamcommunity.com](https://steamcommunity.com/workshop/filedetails/?l=tchinese&id=2987081908)

# 总结

吾辈的启动项：-vulkan -novid -console +m_rawinput 1 -heapsize 6000000 -processheap -high -num_edicts 4096

然后，**一定**要替换`dxvk_d3d9.dll`，详细办法见[使用 DXVK 使 Vulkan API 效率更高](#使用-dxvk-使-vulkan-api-效率更高)，启动项一定要加`-vulkan`


# 原文
本收藏為個人自用的遊戲優化方法、指令、管理模組之用途。

我需要紀錄我是如何「自定義」遊戲內容，並做個資訊彙總，也助於有看見此收藏的玩家們（不保證 100% 對大家有效）。

## 啟動選項（Launch Options）

### 版本一

-vulkan -autoconfig -lv -heapsize 6000000 -novid -processheap -high -num_edicts 4096 

-heapsize 调动内存
-novid 自动跳过开头动画
-lv 低血腥模式，千万不要开清理尸体
-autoconfig 解决核显玩家游戏黑的问题
-num_edicts 给求生最大内存缓存 -heapsize不能大于-num_edicts（不然会加载进不去地图,换算单位，600万=4096）
-processheap：这个指令要求游戏使用指定的堆进行内存分配
high：将游戏的进程优先级设置为“高”，给予CPU最高优先级

### 版本二

我個人使用的：

-novid -console +m_rawinput 1 +cl_crosshair_alpha 0

啟動選項個別說明：

*   -novid：跳過遊戲片頭動畫。99% 的玩家必定要輸入的指令之一，節省你的時間。
*   -console：啟動時自動開啟控制台。只是為了方便看控制台，非必要參數。
*   +m_rawinput 1：啟用 Raw Input，讓遊戲直接讀滑鼠輸入，降低受 Windows 指標加速 / 敏感度干擾的機率。
*   +cl_crosshair_alpha 0：關閉遊戲內準心，用於 Addons 的自定義準心。
*   -insecure：進入不安全模式。有修改遊戲的腳本 Addons，這是必要指令，因為你需要讓腳本 Addons「正常執行」，這對於開啟「本地伺服器」的主機玩家來說有幫助。（注意，這將會無法連接 Valve 官方伺服器）。
*   -vulkan：使用 Vulkan API 渲染遊戲。助於降低 CPU 使用率，也『可能』降低 RAM 使用率，一般來說這是給 Mac 和 Linux 系統使用的 API，有人實測 Vulkan API 在 Windows 系統下有「優化」的感覺，非必要選項，可嘗試。  
    DirectX9 vs Vulkan(DXVK 2.6.1)：  
    [https://www.youtube.com/watch?v=tRX-GR0hhvk](https://www.youtube.com/watch?v=tRX-GR0hhvk)

縮短遊戲載入時間

訂閱的 Addons 下載完成後，都放入 Addons 資料夾，並取消訂閱

實際做法是：

1.  訂閱一個 Addons 後進入遊戲。  
    
2.  遊戲自動下載該 Addons，下載完畢後關閉遊戲。  
    
3.  進入到「left4dead2」資料夾的「addons」。  
    
4.  將「workshop」資料夾內的所有檔案複製到上一層「addons」資料夾，並取消訂閱所有 Addons。  
    
5.  重啟遊戲發現不再檢查 Addons 更新，這使遊戲啟動速度更快。

為何每次開遊戲都在等 Addons 載入？原因就是 L4D2 會自動檢查訂閱 Addons 是否需要更新，而訂閱越多 Addons 載入越久。其實不是每個 Addons 都需要一直更新。  
[從此 Reddit 文章的回覆中習得到的方法。](http://www.reddit.com/r/l4d2/comments/1392qc0/addons_on_startup_in_left_4_dead_2/#:~:text=addon%20folder%20and%20then%20unsubscribe)

終極 CFG 最佳設置

[The Ultimate Left 4 Dead 2 Config (autoexec) by J.](http://github.com/theletterjwithadot/Ultimate-Config-for-L4D2) [github.com]，是由 J 為 L4D2 修改的 CFG 配置檔，這是他花大量心血與時間研究出的終極方案。

## 使用 DXVK 使 Vulkan API 效率更高

Vulkan API 透過 [DXVK](http://github.com/doitsujin/dxvk/releases) [github.com] 使轉換效率越來越高，效能可能比 DirectX API 還要高。

安裝方法：

1.  下載最新版本的 [DXVK](http://github.com/doitsujin/dxvk/releases) [github.com] tar.gz 壓縮檔。  
    
2.  進到 tar.gz 壓縮檔內，路徑：「drvk - 版本號」資料夾 → 「x32」資料夾 → 複製「d3d9.dll」檔案  
    
3.  打開「Left 4 Dead 2」資料夾 → 「bin」資料夾 → 先備份「dxvk_d3d9.dll」檔案 → 再用「d3d9.dll」去取代原始「dxvk_d3d9.dll」，記得檔案命名為「dxvk_d3d9.dll」。  
    
4.  L4D2 啟動選項一定要添加`-vulkan`
    

測試方法：

非常簡單，打開遊戲後設定視窗化，並查看視窗名稱是否有「-vulkan」字樣，有就是成功了。

！免責聲明！

任何修改遊戲之行為導致帳戶被 Ben，由當事人自行承擔。