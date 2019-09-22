const path = require('path');

const DJANGO_STATIC = path.resolve(__dirname, "../../static/");

module.exports = (env, args) => {
	const config = {
		entry: "./src/index.tsx",
		output: {
			path: DJANGO_STATIC,
			filename: "bundle.js"
		},
		resolve: {
			extensions: [".ts", ".tsx", ".js", ".jsx"]
		},
		module: {
			rules: [
				{
					test: /\.tsx?$/,
					loader: "ts-loader"
				}
			]
		}
	};
	const sass = {
		entry: "./src/index.scss",
		output: {
			path: DJANGO_STATIC,
			filename: "index.css"
		},
		resolve: {
			alias: {
				DJANGO_STATIC: DJANGO_STATIC
			},
			extensions: [".scss", ".css"]
		},
		module: {
			rules: [
				{
					test: /\.scss?$/,
					loader: ["style-loader", "css-loader", "sass-loader"]
				}
			]
		}
	};
	return [config, sass];
}
