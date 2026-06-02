# TeamSpeak SDK for Unreal Engine

Add proven, low-latency TeamSpeak voice communication to your Unreal Engine project.


## Repository layout

| Path | Description |
|------|-------------|
| `Plugins/` | The TeamSpeak SDK Unreal plugin (`teamspeak-sdk-unreal`), included as a git submodule. Wraps the native TeamSpeak SDK C API with C++ and Blueprint APIs and routes audio through Unreal's audio mixer. See [`Plugins/README.md`](Plugins/README.md). |
| `TeamSpeakMinimal/` | A minimal Unreal project: a main-menu UI to connect to a server, input/output mute toggles, and voice routed through the engine. The smallest end-to-end integration. |
| `bootstrap.py` | One-command setup — initializes the plugin submodule and downloads the TeamSpeak SDK binaries it needs. |

## Getting started

### 1. Clone (recursively)

```
git clone --recursive <repo-url>
```

Already cloned without `--recursive`? The bootstrap step below initializes the submodule for you.

### 2. Bootstrap

From the repository root:

```
python bootstrap.py
```

This runs `git submodule update --init --recursive`, then downloads the TeamSpeak SDK
(version pinned in `Plugins/bootstrap_config.json`) into `Plugins/TeamSpeak_SDK/ThirdParty/`.
The SDK binaries are intentionally **not** committed, so this step is required before the
project will build.

### 3. Open & build

Open `TeamSpeakMinimal/TeamSpeakMinimal.uproject` in Unreal Engine 5 and let it compile the
`TeamSpeak_SDK` module, or build from the command line (the editor must be closed — Live
Coding holds the module lock otherwise):

```
"<UE>/Engine/Build/BatchFiles/Build.bat" TeamSpeakMinimalEditor Win64 Development -Project="<abs-path>/TeamSpeakMinimal/TeamSpeakMinimal.uproject" -WaitMutex
```

### 4. Run

Play the level, enter a server address (with channel / password as needed) in the menu, and
connect. Voice is captured from your default input device and played back through Unreal's
audio mixer; the UI exposes input and output mute toggles.

## Requirements

- Unreal Engine 5
- Python 3 (for `bootstrap.py`)
- A TeamSpeak SDK server to connect to (the server binary ships with the TeamSpeak SDK download)
- Supported platforms: Win64, Linux, macOS, Android, iOS

## Using the plugin in your own project

The plugin is maintained in its own repository and consumed here as the `Plugins/` submodule,
so you can drop it into any Unreal project independently of this sample. For the C++/Blueprint
API, the audio-mixer bridge, and the `ThirdParty` layout, see [`Plugins/README.md`](Plugins/README.md).

## License

Use of the TeamSpeak SDK is governed by the TeamSpeak SDK license — see
[`Plugins/LICENSE.md`](Plugins/LICENSE.md) and https://www.teamspeak.com/downloads#sdk.
