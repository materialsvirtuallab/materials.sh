cd conda-skeleton/platform
% FOR %%A IN (latexcodec tabulate monty pybtex palettable spglib pydispatcher pymatgen) DO conda skeleton pypi %%A
% FOR %%A IN (latexcodec tabulate monty pybtex palettable spglib pydispatcher pymatgen) DO conda build %%A
FOR %%A IN (spglib) DO conda build %%A
FOR %%A IN (spglib) DO anaconda upload -u matsci %HOMEPATH%\Miniconda3\win-64\%AA-*py35*.tar.bz2
