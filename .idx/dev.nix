# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
    packages = [
    pkgs.sudo
    pkgs.python3
    pkgs.python311Packages.pip
  #  pkgs.python311Packages.fastapi
  #  pkgs.python311Packages.uvicorn
    pkgs.pipenv
    pkgs.nodejs_20
    pkgs.nodePackages.nodemon
    pkgs.gh
    pkgs.git
    pkgs.curl
  ];

  # Sets environment variables in the workspace
  env = {};
   idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [ "ms-python.python" "rangav.vscode-thunder-client" ];
    workspace = {
      # Runs when a workspace is first created with this `dev.nix` file
      onCreate = {
        create-venv = ''
          python -m venv $HOME/.venv/
          source $HOME/.venv/bin/activate
          pip install -r requirements.txt
        '';
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "streamlit_app.py" ];
      };
      # To run something each time the workspace is (re)started, use the `onStart` hook
    };
  };
}
