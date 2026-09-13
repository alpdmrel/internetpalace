import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
// Astro deprecates re-exporting `z`; import it from zod directly.
import { z } from 'zod';

/**
 * Status drives grouping and the colour of the badge on cards.
 * `shipped`   - built, installed and in daily use
 * `active`    - currently being built
 * `on-hold`   - designed, parked before assembly
 * `research`  - academic / written work
 * `archived`  - superseded by a later revision
 */
const status = z.enum(['shipped', 'active', 'on-hold', 'research', 'archived']);

const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    tagline: z.string(),
    year: z.string(),
    status,
    domain: z.enum(['Home Automation', 'Instrumentation', 'Mechanical', 'Power', 'Academic']),
    tech: z.array(z.string()).default([]),
    highlights: z.array(z.string()).default([]),
    /** Key into src/data/figures.json for a captioned figure gallery. */
    figures: z.string().optional(),
    /** Ordering within a status group; lower sorts first. */
    order: z.number().default(50),
    featured: z.boolean().default(false),
    /**
     * Optional interactive 3D model. Drop a .glb in public/models/ and fill
     * this in — the project page renders a viewer with orbit + explode.
     */
    model: z
      .object({
        src: z.string(),
        caption: z.string().optional(),
        /** Distance multiplier applied when the exploded view is toggled. */
        explode: z.number().default(1.6),
        /** Vertical offset applied to frame the model. */
        yOffset: z.number().default(0),
      })
      .optional(),
  }),
});

export const collections = { projects };
