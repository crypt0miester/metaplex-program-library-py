# mpl-candy-machine
#

This package contains the Candy Machine contract SDK code in Python3.9. This MPL package targets the current generation of candy machine on the v2.0.0 release line.

## Developing

In order to update the generated SDK when the rust contract was updated please run:

```
anchorpy client-gen ./idl/candy_machine.json ./src --program-id cndy3Z4yapfJBmL3ShUp5exZKqR3z33thTzeNMm2gRZ
```
Make sure you have anchorpy[cli] installed

## LICENSE

Apache v2.0
