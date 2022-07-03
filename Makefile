create-project-wordlist:
	cspell --words-only --unique '**/*.{py,c,cpp,h,md,rst}' | LC_ALL='C' sort --ignore-case > project-words.txt

.PHONY: *