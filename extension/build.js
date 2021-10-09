const esbuild = require("esbuild");
const fs = require("fs");
const path = require("path");

const isDevelopment = process.argv.length >= 3 && process.argv[2] === "dev" || process.env.NODE_ENV === 'development';

const staticFiles = ["manifest.json", "popup.html", "style.css"];

esbuild
  .build({
    entryPoints: ["popup.ts", "lieferando.ts"].map((filename) =>
      path.join("src", filename)
    ),
    outbase: "src",
    outdir: "dist",
    bundle: true,
    target: "esnext",
    treeShaking: true,
    platform: "browser",
    logLevel: "info",

    plugins: [
      {
        name: "Static files",
        setup: (build) => {
          build.onEnd(async () => {
            for (let staticFile of staticFiles) {
              await new Promise((resolve) =>
                fs.copyFile(
                  path.join("src", staticFile),
                  path.join("dist", staticFile),
                  resolve
                )
              );
            }
            return null;
          });
        },
      },
    ],

    // Development
    ...(isDevelopment ? { sourcemap: "inline", incremental: true } : {}),
  })
  .then((build) => {
    console.log("Build complete!");
    // Manual hot reload to also cover the static files
    if (isDevelopment) {
      fs.watchFile("src", async () => {
        console.log("Rebuilding...");
        await build.rebuild();
        console.log("Rebuild complete!");
      });
    }
  })
  .catch(console.error);
