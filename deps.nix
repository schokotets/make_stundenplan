with import <nixpkgs> {};

runCommand "dummy" {
	buildInputs = [ python310 python310Packages.ortools ];
	PYTHONPATH = "${python310Packages.ortools}/lib/python3.10/site-packages/ortools-9.1.9999-py3.10-linux-x86_64.egg/";
} ""
