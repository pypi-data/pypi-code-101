LANGUAGE_CATALOG_URL = "api/nlu/v1/supported-languages"
CREATE_EXAMPLE_URL = "api/nlu/v1/single/example"
CREATE_PROJECT_URL = "api/nlu/v1/project"
LIST_PROJECTS_URL = "api/nlu/v1/list/projects"
LIST_EXAMPLES_URL = "api/nlu/v1/list/example"
DELETE_EXAMPLE_URL = "api/nlu/v1/example"
DELETE_PROJECT_URL = "api/nlu/v1/single/project"
TRAIN_MODEL_URL = "api/nlu/v1/model/train/queue"
SINGLE_MODEL_DETAILS_URL = "api/nlu/v1/model"
LIST_MODELS_URL = "api/nlu/v1/list/model"
DEPLOY_MODEL_URL = "api/nlu/v1/model/deploy"
DELETE_MODELS_URL = "api/nlu/v1/model"
PARSE_URL = "api/nlu/v1/model/parse"

TRAINING_PROGRESS = [
    "Initiated",
    "Queued",
    "Preparing Data",
    "Data Prepared",
    "Pipeline Building",
    "Pipeline Built",
    "Training",
    "Trained",
    "Saved",
    "Completed",
]

SUPPORTED_LANGUAGES = [
    "eu",
    "be",
    "ca",
    "hr",
    "cs",
    "et",
    "gl",
    "hu",
    "ga",
    "la",
    "lv",
    "sr",
    "sk",
    "sl",
    "bg",
    "hy",
    "tr",
    "uk",
    "he",
    "kk",
    "mt",
    "ug",
    "fi",
    "sv",
    "id",
    "ko",
    "vi",
    "af",
    "hi",
    "bn",
    "te",
    "ta",
    "mr",
    "ur",
    "gu",
    "kn",
    "ml",
    "as",
    "pa",
    "fa",
    "ar",
    "el",
    "da",
    "en",
    "nb",
    "zh",
    "nl",
    "fr",
    "de",
    "it",
    "ja",
    "lt",
    "pl",
    "pt",
    "ro",
    "ru",
    "es",
    "sq",
    "an",
    "az",
    "ba",
    "bs",
    "br",
    "my",
    "ce",
    "cv",
    "ka",
    "ht",
    "is",
    "io",
    "jv",
    "ky",
    "lb",
    "mk",
    "mg",
    "ms",
    "ne",
    "oc",
    "su",
    "sw",
    "tl",
    "tg",
    "tt",
    "uz",
    "vo",
    "cy",
    "yo",
    "multilingual",
]

# Training status colour codes
C_INITIATED = "⚪"
C_QUEUED = "🔵"
C_COMPLETED = "🟢"
C_TRAINING = "🟠"
C_FAILED = "🔴"
C_TIMED_OUT = "🟤"
C_DEAD = "⚫"
