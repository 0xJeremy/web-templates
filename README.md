# web-templates -- Starter Kits for Web Dev Projects 
### Created by: Ben London and Jeremy Kanovsky


## Dependencies
In this folder are dependencies that can be easily pulled into projects, and are ready to go without any setup.

In the `bootstrap` folder are all the JS and CSS files used in Bootstrap 4.
In the `python` folder are some useful python modules, and wrappers for existing classes.
In the `graphics` folder are some JavaScript libraries (minified) useful in making advanced graphics
In the `utils` folder are some miscellaneous JavaScript libraries that can come in handy when developing a web app.


## React_Express_Node
This folder is a complete project kit for a webapp using React.js for the front end, and powered by an Node.js app with Express.
This folder can be extracted in isolation from the repository to begin projects using these libraries.

 __Setup (requires node and npm to be installed)__
 - Navigate to React_Express_Node/server
 Run "npm install"
 - Navigate to React_Express_Node/client
	Run "npm install"
- (if prompted) run "npm audit" to view problems and then "npm audit fix" to fix them

__Running Web App__
- Navigate to React_Express_Node/server/src
- run "npm run serve"
	- Wait for webpack to build
	- Open browser and goto localhost:8080