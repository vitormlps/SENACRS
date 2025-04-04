/// <reference types='vite/client' />
/// <reference types='vite-plugin-svgr/client' />

interface ImportMetaEnv {
    readonly VITE_API_URL: string
    readonly VITE_API_PREFIX: string
    readonly VITE_AUTH_PREFIX: string
}

interface ImportMeta {
    readonly env: ImportMetaEnv
}