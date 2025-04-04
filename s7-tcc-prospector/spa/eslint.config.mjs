import { fixupConfigRules } from '@eslint/compat';
import reactRefresh from 'eslint-plugin-react-refresh';
import stylisticTs from '@stylistic/eslint-plugin-ts';
import globals from 'globals';
import tsParser from '@typescript-eslint/parser';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import js from '@eslint/js';
import { FlatCompat } from '@eslint/eslintrc';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const compat = new FlatCompat({
	baseDirectory: __dirname,
	recommendedConfig: js.configs.recommended,
	allConfig: js.configs.all,
});

export default [
	{ ignores: ['**/dist', '**/.eslintrc.cjs'] },
	...fixupConfigRules(
		compat.extends(
			'eslint:recommended',
			'plugin:@typescript-eslint/recommended',
			'plugin:react-hooks/recommended'
		)
	),
	{
		plugins: {
			'react-refresh': reactRefresh,
			'@stylistic/ts': stylisticTs,
		},

		languageOptions: {
			globals: { ...globals.browser },

			parser: tsParser,
		},

		rules: {
			'react-refresh/only-export-components': ['warn', { allowConstantExport: true }],

			curly: ['error'],
			'@stylistic/ts/indent': ['error', 4],
			'brace-style': ['error', 'allman'],

			// 'object-curly-newline': ['warn', {multiline: true,}],

			quotes: ['warn', 'single'],
			eqeqeq: ['error', 'always'],
			'@typescript-eslint/no-explicit-any': 'error',
			'semi-style': ['error', 'last'],
			semi: ['error'],
		},
	},
];
