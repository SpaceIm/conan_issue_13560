# Minimal reproducible example of [conan issue 13560](https://github.com/conan-io/conan/issues/13560)

- libA_issue13560 provides a lib without dependencies.
- libB_issue13560 provides a lib with libA_issue13560 as a private dependency.
- libC_issue13560 provides a lib  AND an executable.
  libB_issue13560 is a private dependency of the lib, and this lib is a private dependency of the executable.

On Linux with gcc:

```shell
conan create libA_issue13560 --version "1.0.0" -o "*:shared=True"
conan create libB_issue13560 --version "1.0.0" -o "*:shared=True"
conan create libC_issue13560 --version "1.0.0" -o "*:shared=True"
```

Link errors while building libC_issue13560:

```log
[4/4] Linking CXX executable execC_issue_13560
FAILED: execC_issue_13560
: && /usr/bin/g++-12 -m64 -O3 -DNDEBUG -m64 CMakeFiles/execC_issue_13560.dir/execC_issue13560.cpp.o -o execC_issue_13560  -Wl,-rpath,/home/spaceim/.conan2/p/t/libc_0ac2237a021a8/b/build/Release:  liblibC_issue13560.so && :
/usr/bin/ld: warning: liblibA_issue13560.so, needed by /home/spaceim/.conan2/p/libb_581bbf99dcd92/p/lib/liblibB_issue13560.so, not found (try using -rpath or -rpath-link)
/usr/bin/ld: /home/spaceim/.conan2/p/libb_581bbf99dcd92/p/lib/liblibB_issue13560.so: undefined reference to `libA_issue13560::libA_issue13560_function()'
collect2: error: ld returned 1 exit status
ninja: build stopped: subcommand failed.
```