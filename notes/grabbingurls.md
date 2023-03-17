Grabbing Data URLS
---
> Grabbing Basic Project Data
```
https://api.scratch.mit.edu/projects/[Project ID]
```
> Grabing Cloud Data (Logged Cloud Variable Changes)
```
https://clouddata.scratch.mit.edu/logs?projectid=[Project ID]&limit=[Limit]&offset=0
```
Note: [Limit] is how many changes to the cloud want to be logged. Test by running through each limit from one until an error occurs.
> Grabbing Project JSON File
```
https://api.scratch.mit.edu/projects/[Project ID]
```
