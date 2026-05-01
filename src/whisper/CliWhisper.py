from dataclasses import dataclass
from typing import TypedDict


class TypesArg(TypedDict):
    n_int:int
    n_float:float
    fname:str
    lang:str
    value_bool:bool

    COMMAND:str


@dataclass
class Configroces():

    threads: TypesArg = {'n_int':4,'COMAND':'-t'}
    processors: TypesArg = {'n_int':4, 'COMAND':'-p'}
    disable_gpu:  TypesArg  = {'value_bool':False, 'COMMAND':'-ng'}
    gpu_device_id: TypesArg = {'n_int':'0', 'COMMAND':'-ng'}

    
@dataclass 
class ConfigAudio():

    time_offset_in_milliseconds:TypesArg = {'n_int':0, "COMMAND":'-ot'}
    duration_of_audio_to_process_in_ms:TypesArg = {'n_int':0, "COMMAND":'-d'}
    audio_context_size:TypesArg = {'n_int':0,"COMMAND":'-ac'}

@dataclass 
class ConfigOut():
    
    output_txt:TypesArg= {'value_bool':True,'COMMAND':'-otxt'}
    output_vtt:TypesArg= {'value_bool':False,'COMMAND':'-ovtt'}
    output_srt:TypesArg= {'value_bool':False,'COMMAND':'-osrt'}
    output_lrc:TypesArg= {'value_bool':False,'COMMAND':'-olrc'}
    output_csv: TypesArg = {'value_bool':False,'COMMAND':'-ocsv'}     
    output_json: TypesArg = {'value_bool':False,'COMMAND':'-oj'}     
    output_json_full: TypesArg = {'value_bool':False,'COMMAND':'-ojf'} 
    output_file: TypesArg = {'fname':'tgd ','COMMAND':'-of'} 
    output_words:TypesArg = {'value_bool':False,'COMMAND':'-owts'} 
    font_path_for_Karaoke:TypesArg = {'fname':'/System/Library/Fonts/Supplemental/Courier New Bold.ttf','COMMAND':'-fp'}

@dataclass
class ConfigWords():
    maximum_segment_length_in_characters:TypesArg = {'n_int':0,"COMMAND":"-ml"}
    translate_from_source_language_to_english:TypesArg = {'value_bool':False, "COMMAND":"-tr"}
    split_on_word:TypesArg = {'n_int':-1,'COMMAND': '-sow'} 


@dataclass
class ConfigTrans():
    model:TypesArg = {'fname':'/','COMMAND':'-m'}


@dataclass
class ConfigInput():
    input_audio_file_path:TypesArg = {'fname':'/','COMMAND':'-f'}
    language:TypesArg = {'lang':'auto', 'COMMAND':'-l'}


@dataclass 
class ConfigVad():
    vad:TypesArg ={'value_bool':'False','COMMAND':'--vad'}
    va_model:TypesArg = {'fname':'/', 'COMMAND':' -vm'}
    vad_threshold:TypesArg = {'n_float':'0.5','COMMAND':'-vd'}
    vad_min_speech_duration_ms:TypesArg = {'n_int':'250', 'COMMAND':'-vspd'}
    vad_min_silence_duration_ms:TypesArg = {'n_int':'100','COMMAND':'-vsd'}
    vad_max_speech_duration_s:TypesArg = {'n_int':'-0','COMMAND':' -vmsd'} 
    vad_speech_pad_ms:TypesArg = {'n_int':30,'COMMAND':'-vp'}
    vad_samples_overlap:TypesArg = {'n_float':'0.10','COMMAND':'-vo'}





















'''
  -h,        --help                 [default] show this help message and exit


  -on N,     --offset-n N           [0      ] segment index offset

  -mc N,     --max-context N        [-1     ] maximum number of text context tokens to store

  -bo N,     --best-of N            [5      ] number of best candidates to keep
  -bs N,     --beam-size N          [5      ] beam size for beam search

  -wt N,     --word-thold N         [0.01   ] word timestamp probability threshold
  -et N,     --entropy-thold N      [2.40   ] entropy threshold for decoder fail
  -lpt N,    --logprob-thold N      [-1.00  ] log probability threshold for decoder fail
  -nth N,    --no-speech-thold N    [0.60   ] no speech threshold
  -tp,       --temperature N        [0.00   ] The sampling temperature, between 0 and 1
  -tpi,      --temperature-inc N    [0.20   ] The increment of temperature, between 0 and 1
  -debug,    --debug-mode           [false  ] enable debug mode (eg. dump log_mel)
  
  -di,       --diarize              [false  ] stereo audio diarization
  -tdrz,     --tinydiarize          [false  ] enable tinydiarize (requires a tdrz model)
  -nf,       --no-fallback          [false  ] do not use temperature fallback while decoding
 
  


  
  -np,       --no-prints            [false  ] do not print anything other than the results
  -ps,       --print-special        [false  ] print special tokens
  -pc,       --print-colors         [false  ] print colors
             --print-confidence     [false  ] print confidence
  -pp,       --print-progress       [false  ] print progress
  -nt,       --no-timestamps        [false  ] do not print timestamps

  

  -dl,       --detect-language      [false  ] exit after automatically detecting language

             --prompt PROMPT        [       ] initial prompt (max n_text_ctx/2 tokens)
             --carry-initial-prompt [false  ] always prepend initial prompt
 
   
  -oved D,   --ov-e-device DNAME    [CPU    ] the OpenVINO device used for encode inference
  -dtw MODEL --dtw MODEL            [       ] compute token-level timestamps
  -ls,       --log-score            [false  ] log best decoder scores of tokens


  -fa,       --flash-attn           [true   ] enable flash attention
  -nfa,      --no-flash-attn        [false  ] disable flash attention
  -sns,      --suppress-nst         [false  ] suppress non-speech tokens
  --suppress-regex REGEX            [       ] regular expression matching tokens to suppress
  --grammar GRAMMAR                 [       ] GBNF grammar to guide decoding
  --grammar-rule RULE               [       ] top-level GBNF grammar rule name
  --grammar-penalty N               [100.0  ] scales down logits of nongrammar tokens
'''

