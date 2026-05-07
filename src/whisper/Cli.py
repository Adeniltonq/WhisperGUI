from dataclasses import dataclass,field
from typing import TypedDict 


class TypesArg(TypedDict, total=False):
    n_int:int
    n_float:float
    fname:str
    lang:str
    value_bool:bool
    prompt:str

    COMMAND:str


@dataclass
class ConfigProcess():

    threads: TypesArg = field(default_factory= lambda: {'n_int':4,'COMMAND':'-t'})
    processors: TypesArg = field(default_factory= lambda: {'n_int':4, 'COMMAND':'-p'})
    disable_gpu:  TypesArg  = field(default_factory= lambda: {'value_bool':False, 'COMMAND':'-ng'})
    gpu_device_id: TypesArg = field(default_factory= lambda: {'n_int':0, 'COMMAND':'-ng'})

    
@dataclass 
class ConfigAudio():

    time_offset_in_milliseconds:TypesArg = field(default_factory= lambda: {'n_int':0, "COMMAND":'-ot'})
    duration_of_audio_to_process_in_ms:TypesArg = field(default_factory= lambda: {'n_int':0, "COMMAND":'-d'})
    audio_context_size:TypesArg = field(default_factory= lambda: {'n_int':0,"COMMAND":'-ac'})

@dataclass 
class ConfigOut():
    output_txt:TypesArg= field(default_factory= lambda: {'value_bool':True,'COMMAND':'-otxt'})
    output_vtt:TypesArg= field(default_factory= lambda: {'value_bool':False,'COMMAND':'-ovtt'})
    output_srt:TypesArg= field(default_factory= lambda: {'value_bool':False,'COMMAND':'-osrt'})
    output_lrc:TypesArg= field(default_factory= lambda: {'value_bool':False,'COMMAND':'-olrc'})
    output_csv: TypesArg = field(default_factory= lambda: {'value_bool':False,'COMMAND':'-ocsv'} )    
    output_json: TypesArg = field(default_factory= lambda: {'value_bool':False,'COMMAND':'-oj'})     
    output_json_full: TypesArg = field(default_factory= lambda: {'value_bool':False,'COMMAND':'-ojf'} )
    output_file: TypesArg = field(default_factory= lambda: {'fname':'tgd ','COMMAND':'-of'} )
    output_words:TypesArg = field(default_factory= lambda: {'value_bool':False,'COMMAND':'-owts'} )
    font_path_for_Karaoke:TypesArg = field(default_factory= lambda: {'fname':'/System/Library/Fonts/Supplemental/Courier New Bold.ttf','COMMAND':'-fp'})


@dataclass
class ConfigWords():
    maximum_segment_length_in_characters:TypesArg = field(default_factory= lambda: {'n_int':0,"COMMAND":"-ml"})
    translate_from_source_language_to_english:TypesArg = field(default_factory= lambda: {'value_bool':False, "COMMAND":"-tr"})
    split_on_word:TypesArg = field(default_factory= lambda: {'n_int':-1,'COMMAND': '-sow'} )


@dataclass
class ConfigTrans():
    model:TypesArg = field(default_factory= lambda: {'fname':'/','COMMAND':'-m'})
    best_of:TypesArg = field(default_factory= lambda: {'n_int':5,'COMMAND':'-bo'})
    word_thold:TypesArg = field(default_factory=lambda: {'n_float':0.01,'COMMAND':'-wt'})
    entropy_thold:TypesArg = field(default_factory=lambda: {'n_float':2.40,'COMMAND':'-et'})
    logprob_thold:TypesArg = field(default_factory=lambda: {'n_float':-1.0,'COMMAND':'-lpt'})
    prompt:TypesArg = field(default_factory=lambda: {'prompt':'','COMMAND':'--prompt'})
    beam_size:TypesArg = field(default_factory= lambda: {'n_int':5,'COMMAND':'-bs'})
    temperature:TypesArg = field(default_factory= lambda: {'n_float':0,'COMMAND':'-tp'}) # between 0 and 1
    no_speech_thold:TypesArg = field(default_factory= lambda: {'n_int':0.60,'COMMAND':'-nth'}) # between 0 and 1
    temperature_inc:TypesArg = field(default_factory= lambda: {'n_float':0.20,'COMMAND':'-tpi'}) # between 0 and 1
    diarize:TypesArg = field(default_factory= lambda: {'value_bool':False,'COMMAND':'-di'})
    max_context:TypesArg = field(default_factory= lambda: {'n_int':-1,'COMMAND': '-mc'})


@dataclass
class ConfigInput():
    input_audio_file_path:TypesArg = field(default_factory= lambda: {'fname':'/','COMMAND':'-f'})
    language:TypesArg = field(default_factory= lambda: {'lang':'auto', 'COMMAND':'-l'})


@dataclass 
class ConfigVad():
    vad:TypesArg =field(default_factory= lambda: {'value_bool':'False','COMMAND':'--vad'}) 
    va_model:TypesArg = field(default_factory= lambda: {'fname':'/', 'COMMAND':'-vm'})
    vad_threshold:TypesArg = field(default_factory= lambda: {'n_float':0.5,'COMMAND':'-vd'})
    vad_min_speech_duration_ms:TypesArg = field(default_factory= lambda: {'n_int':250, 'COMMAND':'-vspd'}) # (0.0-1.0)
    vad_min_silence_duration_ms:TypesArg = field(default_factory= lambda: {'n_int':100,'COMMAND':'-vsd'})
    vad_max_speech_duration_s:TypesArg = field(default_factory= lambda: {'n_int':-0,'COMMAND':'-vmsd'} )
    vad_speech_pad_ms:TypesArg = field(default_factory= lambda: {'n_int':30,'COMMAND':'-vp'})
    vad_samples_overlap:TypesArg = field(default_factory= lambda: {'n_float':0.10,'COMMAND':'-vo'})




@dataclass
class CliWhisper():
    conf_process = ConfigProcess()
    conf_audio = ConfigAudio() 
    conf_out = ConfigOut()
    conf_words = ConfigWords()
    conf_trans = ConfigTrans()
    conf_input = ConfigInput()
    conf_vad = ConfigVad()
    








'''
========================================
WHISPER ADVANCED MODE (TODO / FUTURE)
========================================

CORE CONTROL
----------------------------------------
-on N, --offset-n N [0]
    Segment index offset.
    Usado quando o áudio está dividido em partes.

-debug, --debug-mode [false]
    Ativa modo debug (ex: dump log_mel).

LANGUAGE / FLOW CONTROL
----------------------------------------
-dl, --detect-language [false]
    Detecta idioma automaticamente e encerra.

--carry-initial-prompt [false]
    Sempre reaplica o prompt inicial.

DECODING BEHAVIOR
----------------------------------------
-nf, --no-fallback [false]
    Desativa fallback de temperature (mais determinístico).

-tdrz, --tinydiarize [false]
    Diarização leve (requer modelo tdrz).

AUDIO / TIMESTAMP CONTROL
----------------------------------------
-dtw MODEL
    Timestamps por token via alinhamento fino.

-ls, --log-score [false]
    Log das pontuações do decoder.

OUTPUT CONTROL (DEBUG / VISUAL)
----------------------------------------
-np, --no-prints [false]
    Não imprime nada além do resultado final.

-ps, --print-special [false]
    Mostra tokens especiais.

-pc, --print-colors [false]
    Ativa cores no terminal.

--print-confidence [false]
    Mostra confiança das palavras.

-pp, --print-progress [false]
    Mostra progresso.

-nt, --no-timestamps [false]
    Remove timestamps da saída.

PERFORMANCE / ACCELERATION
----------------------------------------
-oved D, --ov-e-device DNAME [CPU]
    Seleciona dispositivo OpenVINO.

-fa, --flash-attn [true]
    Ativa flash attention (mais rápido).

-nfa, --no-flash-attn [false]
    Desativa flash attention.

FILTERING / CLEANING
----------------------------------------
-sns, --suppress-nst [false]
    Remove tokens não relacionados à fala.

--suppress-regex REGEX
    Remove padrões de tokens via regex.

STRUCTURED OUTPUT (ADVANCED)
----------------------------------------
--grammar GRAMMAR
    Define gramática GBNF para forçar formato.

--grammar-rule RULE
    Regra inicial da gramática.

--grammar-penalty N [100.0]
    Penalidade para tokens fora da gramática.

========================================
NOTES
----------------------------------------
- Este bloco é apenas para referência futura.
- Será reorganizado em "Advanced Mode UI" posteriormente.
- Atualmente não está integrado na GUI principal.
========================================
'''