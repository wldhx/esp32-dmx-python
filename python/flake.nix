{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/22.11";
  };

  outputs = { self, nixpkgs }:
    let
      pkgs = import nixpkgs {
        system = "x86_64-linux";
      };
    in
    with pkgs; {
      devShell.x86_64-linux = mkShell {
        buildInputs = [
	  python311
	  black
	  poetry
        ];
      };
    };
}
