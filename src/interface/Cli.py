from dataclasses import dataclass, field
import tkinter as tk


def tv(value, t="int"):
    if t == "int":
        return tk.IntVar(value=value)
    if t == "float":
        return tk.DoubleVar(value=value)
    if t == "bool":
        return tk.BooleanVar(value=value)
    return tk.StringVar(value=value)


@dataclass
class ConfigProcess:
    threads: dict = field(default_factory=lambda: {
        "var": tv(4, "int"),
        "COMMAND": "-t"
    })

    processors: dict = field(default_factory=lambda: {
        "var": tv(4, "int"),
        "COMMAND": "-p"
    })

    disable_gpu: dict = field(default_factory=lambda: {
        "var": tv(False, "bool"),
        "COMMAND": "-ng"
    })

    gpu_device_id: dict = field(default_factory=lambda: {
        "var": tv(0, "int"),
        "COMMAND": "-gpu-id"
    })

@dataclass
class ConfigAudio:
    time_offset_in_milliseconds: dict = field(default_factory=lambda: {
        "var": tv(0, "int"),
        "COMMAND": "-ot"
    })

    duration_of_audio_to_process_in_ms: dict = field(default_factory=lambda: {
        "var": tv(0, "int"),
        "COMMAND": "-d"
    })

    audio_context_size: dict = field(default_factory=lambda: {
        "var": tv(0, "int"),
        "COMMAND": "-ac"
    })


@dataclass
class ConfigOut:
    output_txt: dict = field(default_factory=lambda: {
        "var": tv(True, "bool"),
        "COMMAND": "-otxt"
    })

    output_vtt: dict = field(default_factory=lambda: {
        "var": tv(False, "bool"),
        "COMMAND": "-ovtt"
    })

    output_srt: dict = field(default_factory=lambda: {
        "var": tv(False, "bool"),
        "COMMAND": "-osrt"
    })

    output_lrc: dict = field(default_factory=lambda: {
        "var": tv(False, "bool"),
        "COMMAND": "-olrc"
    })

    output_csv: dict = field(default_factory=lambda: {
        "var": tv(False, "bool"),
        "COMMAND": "-ocsv"
    })

    output_json: dict = field(default_factory=lambda: {
        "var": tv(False, "bool"),
        "COMMAND": "-oj"
    })

    output_json_full: dict = field(default_factory=lambda: {
        "var": tv(False, "bool"),
        "COMMAND": "-ojf"
    })

    output_file: dict = field(default_factory=lambda: {
        "var": tv("tgd", "str"),
        "COMMAND": "-of"
    })

    output_words: dict = field(default_factory=lambda: {
        "var": tv(False, "bool"),
        "COMMAND": "-owts"
    })

    font_path_for_Karaoke: dict = field(default_factory=lambda: {
        "var": tv(
            "/System/Library/Fonts/Supplemental/Courier New Bold.ttf",
            "str"
        ),
        "COMMAND": "-fp"
    })


@dataclass
class ConfigWords:
    maximum_segment_length_in_characters: dict = field(default_factory=lambda: {
        "var": tv(0, "int"),
        "COMMAND": "-ml"
    })

    split_on_word: dict = field(default_factory=lambda: {
        "var": tv(-1, "int"),
        "COMMAND": "-sow"
    })



@dataclass
class ConfigTrans:
    model: dict = field(default_factory=lambda: {
        "var": tv("/", "str"),
        "COMMAND": "-m"
    })

    best_of: dict = field(default_factory=lambda: {
        "var": tv(5, "int"),
        "COMMAND": "-bo"
    })

    word_thold: dict = field(default_factory=lambda: {
        "var": tv(0.01, "float"),
        "COMMAND": "-wt"
    })

    entropy_thold: dict = field(default_factory=lambda: {
        "var": tv(2.40, "float"),
        "COMMAND": "-et"
    })

    logprob_thold: dict = field(default_factory=lambda: {
        "var": tv(-1.0, "float"),
        "COMMAND": "-lpt"
    })

    prompt: dict = field(default_factory=lambda: {
        "var": tv("", "str"),
        "COMMAND": "--prompt"
    })

    beam_size: dict = field(default_factory=lambda: {
        "var": tv(5, "int"),
        "COMMAND": "-bs"
    })

    temperature: dict = field(default_factory=lambda: {
        "var": tv(0.0, "float"),
        "COMMAND": "-tp"
    })

    no_speech_thold: dict = field(default_factory=lambda: {
        "var": tv(0.60, "float"),
        "COMMAND": "-nth"
    })

    temperature_inc: dict = field(default_factory=lambda: {
        "var": tv(0.20, "float"),
        "COMMAND": "-tpi"
    })

    diarize: dict = field(default_factory=lambda: {
        "var": tv(False, "bool"),
        "COMMAND": "-di"
    })

    max_context: dict = field(default_factory=lambda: {
        "var": tv(-1, "int"),
        "COMMAND": "-mc"
    })


@dataclass
class ConfigInput:
    input_audio_file_path: dict = field(default_factory=lambda: {
        "var": tv("/", "str"),
        "COMMAND": "-f"
    })

    language: dict = field(default_factory=lambda: {
        "var": tv("auto", "str"),
        "COMMAND": "-l"
    })

    translate_from_source_language_to_english: dict = field(default_factory=lambda: {
        "var": tv(False, "bool"),
        "COMMAND": "-tr"
    })


@dataclass
class ConfigVad:
    vad: dict = field(default_factory=lambda: {
        "var": tv(False, "bool"),
        "COMMAND": "--vad"
    })

    va_model: dict = field(default_factory=lambda: {
        "var": tv("/", "str"),
        "COMMAND": "-vm"
    })

    vad_threshold: dict = field(default_factory=lambda: {
        "var": tv(0.5, "float"),
        "COMMAND": "-vd"
    })

    vad_min_speech_duration_ms: dict = field(default_factory=lambda: {
        "var": tv(250, "int"),
        "COMMAND": "-vspd"
    })

    vad_min_silence_duration_ms: dict = field(default_factory=lambda: {
        "var": tv(100, "int"),
        "COMMAND": "-vsd"
    })

    vad_max_speech_duration_s: dict = field(default_factory=lambda: {
        "var": tv(0, "int"),
        "COMMAND": "-vmsd"
    })

    vad_speech_pad_ms: dict = field(default_factory=lambda: {
        "var": tv(30, "int"),
        "COMMAND": "-vp"
    })

    vad_samples_overlap: dict = field(default_factory=lambda: {
        "var": tv(0.10, "float"),
        "COMMAND": "-vo"
    })


@dataclass
class CliWhisper:
    conf_process: ConfigProcess = field(default_factory=ConfigProcess)
    conf_audio: ConfigAudio = field(default_factory=ConfigAudio)
    conf_out: ConfigOut = field(default_factory=ConfigOut)
    conf_words: ConfigWords = field(default_factory=ConfigWords)
    conf_trans: ConfigTrans = field(default_factory=ConfigTrans)
    conf_input: ConfigInput = field(default_factory=ConfigInput)
    conf_vad: ConfigVad = field(default_factory=ConfigVad)

