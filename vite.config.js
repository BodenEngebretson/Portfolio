import { defineConfig } from "vite";
import path from "path";

export default defineConfig(({ command }) => ({
  // Use '/' as base in dev so the vite dev server serves at root.
  // Use '/static/' for production builds so Django can serve built assets.
  base: command === "serve" ? "/" : "/static/",
  server: {
    // ensure dev server runs on a stable port so Django tags hit the right URL
    port: 5174,
    strictPort: true,
    hmr: {
      protocol: "ws",
      host: "localhost",
      port: 5174,
    },
  },
  build: {
    // Where Vite will save its output files.
    // This should be something in your settings.STATICFILES_DIRS
    outDir: path.resolve(__dirname, "./static"),
    emptyOutDir: false, // Preserve the outDir to not clobber Django's other files.
    manifest: "manifest.json",
    rollupOptions: {
      input: {
        index: path.resolve(__dirname, "./front-end/index.js"),
      },
      output: {
        // Output JS bundles to js/ directory with -bundle suffix
        entryFileNames: `js/[name]-bundle.js`,
      },
    },
  },
});
