// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://alpdemirel.tech',
  integrations: [sitemap()],
  // Custom domain serves from the root, so no `base` is needed. If you ever
  // fall back to alpdmrel.github.io/internetpalace, set base: '/internetpalace'.
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
  },
  vite: {
    build: {
      // three.js is only pulled in by the 3D islands; keep it in its own chunk
      // so content pages never pay for it.
      rollupOptions: {
        output: {
          manualChunks(id) {
            if (id.includes('node_modules/three')) return 'three';
          },
        },
      },
    },
  },
});
