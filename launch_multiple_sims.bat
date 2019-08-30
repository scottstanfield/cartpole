for /l %%x in (1, 1, 5) do (
	echo %%x
	start loop.bat %1
	timeout 10
	)