module.exports = {
	root: true,
	env: { browser: true, es2020: true },
	extends: [
		'eslint:recommended',
		'plugin:@typescript-eslint/recommended',
		'plugin:react-hooks/recommended',
	],
	ignorePatterns: ['dist', '.eslintrc.cjs'],
	parser: '@typescript-eslint/parser',
	plugins: ['react-refresh', '@stylistic/ts'],
	rules: {
		'react-refresh/only-export-components': ['warn', { allowConstantExport: true }],
		curly: ['error'],
		'@stylistic/ts/indent': ['error', 4],
		'brace-style': ['error', 'allman'],
		quotes: ['warn', 'single'],
		eqeqeq: ['error', 'always'],
		'@typescript-eslint/no-explicit-any': 'error',
	},
};
