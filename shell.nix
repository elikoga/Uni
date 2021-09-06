{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell {
  # nativeBuildInputs is usually what you want -- tools you need to run
  nativeBuildInputs = [ pkgs.texlive.combined.scheme-full pkgs.python39Packages.pygments ];
}
