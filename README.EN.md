# Okayu button

Okayu button [Site(not deployed yet)](https://button.okayu.me)

Related Links:

* [Nekomata Okayu's Youtube Channel](https://www.youtube.com/channel/UCvaTdHTWBGv3MKj3KVqJVCw)

* [Nekomata Okayu's Twitter](https://twitter.com/nekomataokayu)

* [Nekomata Okayu's Bilibili HomePage](https://space.bilibili.com/412135222?from=search&seid=730740916312043238)

## Contributing

Please fork this project for modification, and after completing the modification, initiate a Pull Request in this project.

### Add or modify voice

**Description**: All voice meta information is stored in [src/voices.json](src/voices.json). To add or modify these voices, you need to modify this file accordingly.

Voice is always in mp3 format and stored in [public/voices](public/voices). The corresponding URL is `voices/`.

For new voice, please use software such as MP3GainGUI for volume standardization. Currently the volume standardized value is 80.

Because this site uses a strong cache strategy, except for `index.html`, files with the same filename, even if modified, will **NEVER** be refreshed by the client. Therefore, the filename of the newly voice, whatever it is new or modified, **MUST** be different from any previous filename.

If you are modifying voice, delete the original file after modification.

### Participate in translation

Please help us translate to English and Japanese!

The language files for the main program are in three .js files named the language name in [src/locales](src/locales).

The language files for voices are in [src/voices.json](src/voices.json).

The corresponding modification can be recognized by the program as a valid translation.

## Deploying a local development environment

This site is developed using Vue + jQuery + Bootstrap 3.

To deploy a local development environment, first install the latest version of Node. Then follow these steps:

1. Clone the code.

2. Go to the code directory and run `npm install`.

3. Run `npm run serve`. During the code modification process, this local development server can immediately reflect the results of the modification.

4. To compile the files for deployment, run `npm run build`, which will generate the `dist` directory. This site is completely static, you can directly deploy the entire `dist` directory.

> To contribute your code to this project, you don't have to compile locally. After passing the test in the development server and pushing it to Github, you can directly require a Pull Request to this project.

## LICENCE

Program: MIT

Audio: According to the [Hololive secondary creation licence](https://www.hololive.tv/terms).

This project is a work of enthusiasts and is not related to the hololive official.

## Special Thanks

This project is supported by MeowSound Idols.

This project is modified based on the [Meamea button](https://github.com/zyzsdy/meamea-button).
