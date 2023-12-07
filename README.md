# process-alert

As [`process-watcher`](https://github.com/arlowhite/process-watcher) does not seem to be maintained anymore, I decided to create `process-alert`.

`process-alert` is a basic python program to get alerted when a process is finished.

Contrary to `process-watcher` you can only monitor one program at a time, otherwise this program would be way more complex with many more `async` coroutines and `await` operations. To monitor many programs, just launch it as many times as you need.
