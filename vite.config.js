import { defineConfig } from "vite";
import path from "path";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig(({ command }) => ({
  plugins: [react(), tailwindcss()],

  // Serve assets under '/static/' for both dev and production so
  // Django and the Vite dev server use the same URL paths.
  base: "/static/",
  build: {
    // Where Vite will save its output files.
    // This should be something in your settings.STATICFILES_DIRS
    outDir: path.resolve(__dirname, "./static"),
    emptyOutDir: false, // Preserve the outDir to not clobber Django's other files.
    manifest: "manifest.json",
    rollupOptions: {
      input: {
        index: path.resolve(__dirname, "./front-end/index.js"),
        hello: path.resolve(__dirname, "./front-end/hello.jsx"),
        style: path.resolve(__dirname, "./front-end/style.css"),
      },
      output: {
        // Output JS bundles to js/ directory with -bundle suffix
        entryFileNames: `js/[name]-bundle.js`,
        assetFileNames: "css/[name].css",
      },
    },
  },
}));
