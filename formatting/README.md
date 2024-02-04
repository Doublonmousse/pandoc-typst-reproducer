Dot support :

- for double dots, uses `\overset{¨}{x}` instead of `\ddot{x}` from the `amsmath` package
- for simple dot, uses `\overset{\cdot}{x}` instead of `\dot{x}` from the `amsmath` package
- when `\underset` is used, the `mathtools` should be in the preamble, for now there isn't a preamble
- for overline, `\underset{¯}{...}` is used instead of `\overline` 
- for norm, the bars are rendered with `\left.\parallel` and there is actually no scaling of the delimiters. `\left\|` and `\right\|` should be used instead
- `tilde(x)` translated to `\overset{\sim}{x}` instead of `\tilde{x}`