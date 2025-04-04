import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';
import svgr from 'vite-plugin-svgr';

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
    const env = loadEnv(mode, process.cwd(), '');

    return {
        define: {
            __API_URL: JSON.stringify(env.VITE_API_URL),
            __API_PREFIX: JSON.stringify(env.VITE_API_PREFIX),
            __AUTH_PREFIX: JSON.stringify(env.VITE_AUTH_PREFIX),
        },
        plugins: [
            react(),
            svgr()
        ],
        assetsInclude: ['**/*.obj', '**/*.mtl', '**/*.exr'],
    
        server: {
            proxy: {
                '/api': {
                    // target: 'http://locahost:8000',
                    target: 'http://92.113.39.44:8000',
                    changeOrigin: true,
                    secure: false,
                    ws: true,
                    rewrite: (path) => path.replace(/^\/api\/v2/, ''),
                },
            },
        },
        build: { sourcemap: true }
    }
});
