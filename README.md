# netRipper
##### script to get saved network and their passwords  


## Description
Netripper uses cmd shell output 
for commands such as 
```
netsh wlan show profiles
```
and
```
netsh wlan show profile name="profilename" key=clear
```
and prints the output in seperate files 
> bonus : also prints ip adress in ness.txt 

in the near future it'll have database implementation probably using Django or emailing system


## Installation

```
cd your/directory/
git clone 'https://github.com/MythicalMayhem/netRipper'
cd netRipper
python netrip.py
```

## Usage
after executing netrip.exe you'll be prompted on the output file location  
>press Enter directly to choose the same directory as netrip.exe

and done

## Example 

The output should be something like this  
![example](https://github.com/MythicalMayhem/netRipper/blob/main/assests/exp.jpg)

## Compatibility
currently netripper is only works on computers with these languages : 
- Frensh
- English


