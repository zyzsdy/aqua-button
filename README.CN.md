# 粥按钮

粥按钮 [网站链接（尚未完成）](https://button.okayu.me)

相关链接:

* [猫又小粥的Youtube频道](https://www.youtube.com/channel/UCvaTdHTWBGv3MKj3KVqJVCw)

* [猫又小粥的Twitter](https://twitter.com/nekomataokayu)

* [猫又小粥的Bilibili空间](https://space.bilibili.com/412135222?from=search&seid=730740916312043238)

## 参与完善本项目

请Fork本项目进行修改，完成修改后在本项目中发起一个Pull Request。

### 添加或修改音频

请各位以文件夹的形式分类，并将音频文件以 中文_日文.mp3 的格式命名后，将文件下载地址贴至issue里，或直接按下列手动编辑后发送Pull request来添加音频。

**简述**: 所有的音频信息都存储在 [src/voices.json](src/voices.json)中. 若要添加或修改音频，你需要对应的修改这个文件。

音频一律采用MP3格式，存储在 [public/voices](public/voices)中.对应的URL为`voices/`.

添加的新音频请先进行音量标准化。可以使用MP3GainGUI之类的软件，目前音量全部标准化为80。

由于本站采用强缓存策略，除`index.html`外,文件名一致的文件，即使进行过修改也**永远** 不会被客户端刷新。因此新添加音频的文件名**必须**和之前的任何文件名都不同。

如果是修改音频，请在修改之后删除原音频文件。

### 参与音频翻译

请为我们英文与日文的翻译工作贡献你的一份力量！

对主程序的翻译请在[src/locales](src/locales)中三个以语言名命名的js文件内进行。

对语音的翻译请在[src/voices.json](src/voices.json)内进行。

相关修改能够自动地被识别为有效的翻译文本并在对应语种界面下生效

## 部署本地开发环境

本站使用 Vue + jQuery + Bootstrap 3 开发。

要部署本地开发环境，请先安装最新版的node。然后按照如下步骤操作：

1. Clone代码到本地。

2. 进入代码目录，运行 `npm install`.

3. 运行本地开发服务器 `npm run serve`，在代码修改过程中，本地开发服务器可以即时反映修改的结果。

4. 要编译可供部署的文件，请运行 `npm run build`,这会生成 `dist`目录。 本站为全静态，将整个`dist`目录部署即可。

> 若要为本项目贡献你的代码，你不必在本地编译。在开发服务器中测试通过并推送至Github后，直接给本项目提交Pull Request即可。

## LICENCE

程序部分：MIT

音频部分：根据 [Hololive二次创作条例](https://www.hololive.tv/terms)进行

本项目为爱好者作品，和hololive官方没有关联

## Special Thanks

This project is supported by MeowSound Idols.

This project is modified based on the [Meamea button](https://github.com/zyzsdy/meamea-button).
