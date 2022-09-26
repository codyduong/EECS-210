# Assignment 3 - Rust

## Delieverables

1. Copy of Rubric2.docx with your name and ID filled out (do not submit a PDF) `.\Rubric 2.docx`
2. Source code. (see `.\src\main.rs`)
3. Screen print showing the successful execution of your code or copy and paste the output from a console screen to a Word document and PDF it. `.\Screenshot.pdf`

## Pre-reqs
* Rust

Install rust here: https://www.rust-lang.org/tools/install
>  * install with `curl`: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
>  * uninstall with `rustup`: `rustup self uninstall`

This was tested on `cargo 1.64.0 (387270bc7 2022-09-16)`, or the LTS.

Rust is supposed to be 100% backwards compatible so should work on any version

## Run from source
If you have cargo/rust
```bash
cargo run
```

## Build from source
Requires `cargo` for compilation.

Rust uses LLVM and should auto-target the correct machine code for your machine.
The built code is then available at `target/release/main`

### make
```bash
make && target/release/main
```

### cargo
```bash
cargo build -r
# The build will be output to `target/release/main`
target/release/main
```


