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

## CLI Usage

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
python3 process_cli.py process_name name geany --email-to me@tdl.com
```

You can add as many email you want, by adding `--email-to another@tld.com` ...

### Matrix

Copy and edit the configuration file:

```bash
cp config/process-alert.conf.sample config/process-alert.conf
vim config/process-alert.conf
```

Enter configuration option for your Matrix room, server URL; you also need a token to post messages.

See [here](https://webapps.stackexchange.com/a/138497) on how to retrieve your user token.

Then, to get alerted with Matrix (need `matrix_` values in the configuration file `config/process-alert.conf`):

```bash
python3 process_cli.py process_name name geany --notifymethod matrix
```

### Mattermost

Setup is a bit more simple as Matrix because you only need to [create a Mattermost webhook](https://developers.mattermost.com/integrate/webhooks/incoming/). Then, add your Mattermost webhook URL to your configuration file `config/process-alert.conf`.

## Using configuration file only


You can use this program without any argument by using `process.py` instead of `process_cli.py`. Your configuration file `config/process-alert.conf` will need to all the required informations.


```bash
source venv_process_alert/bin/activate
cd process-alert

python3 process.py
```

Config file are checked in the following order:

  - `config/process-alert.conf`,
  - `~/.config/process-alert.conf`,
  - `/etc/process-alert/process-alert.conf`.
  