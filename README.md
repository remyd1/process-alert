# process-alert

As [`process-watcher`](https://github.com/arlowhite/process-watcher) does not seem to be maintained anymore, I decided to create `process-alert`.

`process-alert` is a basic python program to get alerted when a process is finished.

Contrary to `process-watcher` you can only monitor one program at a time, otherwise this program would be way more complex with many more `async` coroutines and `await` operations. To monitor many programs, just launch it as many times as you need.

## Install

```bash
python3 -m venv venv_process_alert 
git clone https://github.com/remyd1/process-alert.git
source venv_process_alert/bin/activate

cd process-alert
python3 -m pip install -r requirements.txt
```

## Usage

```bash
source venv_process_alert/bin/activate
cd process-alert
python3 process_cli.py --help
python3 process_cli.py process_name name geany 
```

You will be alerted when geany program will be finished with a desktop notification.

```bash
# to be alerted for PID 11111 to be finished
python3 process_cli.py process_pid num 11111
```

Get alerted with email:

```bash
python3 process_cli.py process_name name geany --email me@tdl.com
```


### Matrix

Copy and edit the configuration file:

```bash
cp config/process-alert.conf.sample config/process-alert.conf
vim config/process-alert.conf
```

Enter configuration option for your Matrix room, server URL; you also need a token to post messages.

Then, to get alerted with Matrix (need `matrix_` values in the configuration file `config/process-alert.conf`):

```bash
python3 process_cli.py process_name name geany --notifymethod matrix
```
