{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell {
  # nativeBuildInputs is usually what you want -- tools you need to run
  nativeBuildInputs = [
    pkgs.texlive.combined.scheme-full
    pkgs.python39Packages.pygments
    pkgs.zlib
    pkgs.stdenv.cc.cc.lib
    pkgs.sqlite.dev
  ];
  shellHook = ''
    # libz.so.1 is in zlib
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${pkgs.lib.makeLibraryPath [ pkgs.zlib pkgs.stdenv.cc.cc.lib ]}
    # . /home/elikoga/Dev/Uni/ITS/ctf/venv/bin/activate
    # . /home/elikoga/Dev/Uni/NLPwDL/venv/bin/activate
  '';
}