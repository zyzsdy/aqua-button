# おかゆボタン（监修中）

おかゆボタン [このリンクをおクリックして](https://aquaminato.moe)

Related Links:

* [猫又おかゆのYouTubeチャンネル](https://www.youtube.com/channel/UCvaTdHTWBGv3MKj3KVqJVCw)

* [猫又おかゆのツイータータイムライン]](https://twitter.com/nekomataokayu)

* [猫又おかゆのビリビリ動画チャンネル](https://space.bilibili.com/412135222?from=search&seid=730740916312043238)

## 贡献

このレポーをフォックして、またご修正をください。完成のプロジェクトをこちらにプールレクエストをください。

### 音声追加と修正

**説明**: 全部の音声データリストは[src/voices.json](src/voices.json)に保存された、音声を追加したうえ, このリストも更新してください。

VoiceはMP3やWAVのフォーマットで[public/voices](public/voices)保存しています。相応のURLは `voices/`です。

新規音声が追加したいなら、ソフトウェアを使て、音量が標準の80に調整してください。

Because this site uses a strong cache strategy, except for `index.html`, files with the same filename, even if modified, will **NEVER** be refreshed by the client. Therefore, the filename of the newly voice, whatever it is new or modified, **MUST** be different from any previous filename.

If you are modifying voice, delete the original file after modification.

### 翻訳仕事を参加

Please help us translate to English and Japanese!

The language files for the main program are in three .js files named the language name in [src/locales](src/locales).

The language files for voices are in [src/voices.json](src/voices.json).

The corresponding modification can be recognized by the program as a valid translation.

## Deploying a local development environment

This site is developed using Vue + jQuery + Bootstrap 3.

To deploy a local development environment, first install the latest version of Node. Then follow these steps:

1. このレポーをコーロンして。

2. プロジェクトフォルダに入って、`npm install`を.

3. `npm run serve`でパソコンにウェブサイトを開け、修正の間に、パソコンのウェブサイトも変われる。

4. To compile the files for deployment, run `npm run build`, which will generate the `dist` directory. This site is completely static, you can directly deploy the entire `dist` directory.

> To contribute your code to this project, you don't have to compile locally. After passing the test in the development server and pushing it to Github, you can directly require a Pull Request to this project.

## ライセンス

プログラム: MIT

音声: [Hololive secondary creation licence](https://www.hololive.tv/terms)を対応.

ただのファン作品ですが、本家のホロライブは関係がありません。

## 特別感謝

このプロジェクトはMeowSound Idolsをご参考しまいました

[Meamea button](https://github.com/zyzsdy/meamea-button)から修正になっております。
