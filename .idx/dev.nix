# This file configures the development environment
# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "unstable"; # or "stable-24.11"

  # Use https://search.nixos.org/packages to find packages
  packages = [
      pkgs.python3
      pkgs.nodejs_23
      pkgs.sqlite3
      pkgs.postgresql
      pkgs.redis
      pkgs.go
      pkgs.docker
      pkgs.docker-compose
      pkgs.sudo
      pkgs.git
      pkgs.gh
  ];
  
  # Sets environment variables in the workspace
  env = {};
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [ "ms-python.python" ];
    workspace = {
      # Runs when a workspace is first created with this `dev.nix` file
      onCreate = {
        setup-env = ''
          python -m venv $HOME/.venv/
          source $HOME/.venv/bin/activate
          echo "export PATH=$HOME/.venv/bin:$PATH" >> $HOME/.bashrc
          pip install uvicorn fastapi
          
          pip install -r requirements.txt
        '';
        # Open the following files by default, if they exist:
        default.openFiles = [ "streamlit_app.py" ];
      };
      # To run something each time the workspace is (re)started, use the `onStart` hook
       onStart = {
          run-migrations = "echo \"Running db migrations\"";
          start-app = "streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0";
       };
    };
  };
}
