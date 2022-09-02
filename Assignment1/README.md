# Assignment 1
Written in Typescript, transpiled to Javascript and compiled using [nexe](https://github.com/nexe/nexe)

## Delieverables
* Copy of rubric at `./Rubric 1.docx`
* See source code screenshot at `./output.pdf`
* Source code in `./src`
  * Contains some artifacts such as `.eslintrc.js` and `package.json` as a natural consequence of using Yarn/NPM with linting rules

## Run from executable
```sh
# linux
dist/Assignment1-x86

# windows (untested)
dist/Assignment1-x64.exe
dist/Assignment1-x86.exe
```

## Run from Source
### With Node and yarn/NPM
* [Node (any LTS version)](https://nodejs.org/en/download/)
* [yarn](https://classic.yarnpkg.com/lang/en/docs/install/#debian-stable)
```sh
yarn install
yarn start
## OR using npm (comes as Node's default package manager)
npm install
npm start
```

### With Deno
https://deno.land/manual@v1.25.0/getting_started/installation
* Deno
```sh
deno run src/index.ts
```