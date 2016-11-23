cd conda-skeletons
FOR %%A IN (latexcodec tabulate monty pybtex palettable spglib pydispatcher pymatgen) DO conda build %%A
FOR %%A IN (latexcodec tabulate monty pybtex palettable spglib pydispatcher pymatgen) DO anaconda upload %HOMEPATH%\Miniconda3\win-64\%%A-*py35*.tar.bz2 -u matsci
cd ..
