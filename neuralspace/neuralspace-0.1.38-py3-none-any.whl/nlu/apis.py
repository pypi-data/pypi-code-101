import json
from asyncio import sleep
from copy import copy
from datetime import datetime
from typing import Any, Dict, List, Text, Tuple

from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    Task,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)
from rich.table import Table
from rich.text import Text as Text_render

from neuralspace.apis import get_async_http_session
from neuralspace.constants import (
    APP_TYPE,
    ARROW_UP,
    AUTHORIZATION,
    BIN,
    BOLD_END,
    BOLD_START,
    BOOK,
    CODE,
    COMMON_HEADERS,
    COMPLETED,
    CONFIDENCE,
    COUNT,
    CREATE_PROJECT_COMMAND,
    CROSS,
    DARK_ORANGE_END,
    DARK_ORANGE_START,
    DATA,
    DEAD,
    DEPLOY_MODEL_COMMAND,
    DOWN_ARROW,
    END,
    END_INDEX,
    ENTITIES,
    ENTITY,
    ENTITY_ACC,
    ERROR,
    EXAMPLE,
    EXAMPLE_ID,
    EXAMPLES,
    FAILED,
    FAST_FORWARD,
    FILTER,
    FINGER_RIGHT,
    GREEN_TICK,
    HASH,
    INFO,
    INITIATED,
    INTENT,
    INTENT_ACCURACY,
    INTENT_CLASSIFIER_METRICS,
    INTENT_RANKING,
    KEY,
    LANGUAGE,
    LANGUAGES,
    LAST_STATUS_UPDATED,
    MESSAGE,
    METRICS,
    MODEL_ID,
    MODEL_NAME,
    MODELS,
    N_REPLICAS,
    NAME,
    NER_METRICS,
    NUMBER_OF_EXAMPLES,
    NUMBER_OF_INTENTS,
    NUMBER_OF_MODELS,
    NUMBERS_IN_SQUARE,
    OM,
    ORANGE_END,
    ORANGE_START,
    PAGE_NUMBER,
    PAGE_SIZE,
    PARSE_MODEL_COMMAND,
    PEN_AND_PAPER,
    PERSON_DUMBELL,
    PERSON_HERE,
    PERSON_STANDING,
    PERSON_TAKING,
    PIN,
    PREPARED,
    PROJECT_ID,
    PROJECT_NAME,
    PROJECTS,
    QUEUED,
    RED_END,
    RED_START,
    REPLICAS,
    SAD_SMILEY,
    SAND_CLOCK,
    SAVED,
    SEARCH,
    SOUP,
    START,
    START_INDEX,
    TEXT,
    TIMED_OUT,
    TRAIN_MODEL_COMMAND,
    TRAINING,
    TRAINING_STATUS,
    TRAINING_TIME,
    TYPE,
    UPLOAD_DATASET_COMMAND,
    WRITING,
    MODEL_ID_key,
    neuralspace_url,
)
from neuralspace.nlu.constants import (
    C_COMPLETED,
    C_DEAD,
    C_FAILED,
    C_INITIATED,
    C_QUEUED,
    C_TIMED_OUT,
    C_TRAINING,
    CREATE_EXAMPLE_URL,
    CREATE_PROJECT_URL,
    DELETE_EXAMPLE_URL,
    DELETE_MODELS_URL,
    DELETE_PROJECT_URL,
    DEPLOY_MODEL_URL,
    LANGUAGE_CATALOG_URL,
    LIST_EXAMPLES_URL,
    LIST_MODELS_URL,
    LIST_PROJECTS_URL,
    PARSE_URL,
    SINGLE_MODEL_DETAILS_URL,
    TRAIN_MODEL_URL,
)
from neuralspace.utils import get_auth_token, is_success_status, print_ner_response

console = Console()


class CustomisedTransferSpeedColumn(TransferSpeedColumn):
    def render(self, task: Task) -> Text_render:
        """Show data transfer speed."""
        speed = task.finished_speed or task.speed
        if speed is None:
            return Text_render("?", style="progress.data.speed")
        return Text_render(f"{speed: .2f} examples/s", style="progress.data.speed")


async def get_languages() -> Dict[Text, Any]:
    console.print(f"> {INFO} {DOWN_ARROW}️ Fetching all supported languages for NLU")
    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()
    async with get_async_http_session().get(
        url=f"{neuralspace_url()}/{LANGUAGE_CATALOG_URL}",
        headers=HEADERS,
    ) as response:
        json_response = await response.json(encoding="utf-8")
        if is_success_status(response.status):
            console.print(f"> {INFO} {GREEN_TICK} Successfully Fetched Languages")
            table = Table()
            table.add_column("Language")
            table.add_column(CODE)
            for row in json_response[DATA]:
                table.add_row(row[LANGUAGE], row[CODE])
            console.print(table)
            console.print(
                f"{FAST_FORWARD} To create the project: {DARK_ORANGE_START}{CREATE_PROJECT_COMMAND}{DARK_ORANGE_END}"
            )
        else:
            console.print(f"> {ERROR} {CROSS} Failed to create project")
            console.print(
                f'''> Reason for failure {SAD_SMILEY}: " {RED_START}{json_response[MESSAGE]}{RED_END} "'''
            )
    return json_response


async def create_project(project_name: Text, languages: List[Text]) -> Dict[Text, Any]:
    console.print(
        f"> {INFO} Creating a project called "
        f"{project_name} in languages: {', '.join(languages)}!"
    )
    payload = {PROJECT_NAME: project_name, LANGUAGE: languages}
    HEADERS = copy(COMMON_HEADERS)
    table = Table()
    HEADERS[AUTHORIZATION] = get_auth_token()
    async with get_async_http_session().post(
        url=f"{neuralspace_url()}/{CREATE_PROJECT_URL}",
        data=json.dumps(payload),
        headers=HEADERS,
    ) as response:
        json_response = await response.json(encoding="utf-8")
        if is_success_status(response.status):
            console.print(f"> {INFO}" f" {KEY} Retrieving credentials from config...")
            console.print(f"> {INFO} " f"{GREEN_TICK} Successfully created project!")
            console.print(
                f"> {INFO} " f"{PERSON_HERE} Here is your project information..."
            )
            table.add_column("Name")
            table.add_column(LANGUAGE)
            table.add_column("App Type")
            table.add_column("Project Id", style="green")
            language_to_write = ""
            for i, language in enumerate(json_response[DATA][LANGUAGE]):
                if i == len(json_response[DATA][LANGUAGE]) - 1:
                    language_to_write += language
                else:
                    language_to_write += language + ", "
            table.add_row(
                json_response[DATA][PROJECT_NAME],
                language_to_write,
                json_response[DATA][APP_TYPE],
                json_response[DATA][PROJECT_ID],
            )
            console.print(table)
            console.print(
                f"{FAST_FORWARD} Upload data to your project using this command:"
                f" {DARK_ORANGE_START}{UPLOAD_DATASET_COMMAND}{DARK_ORANGE_END}"
            )
        else:
            console.print(f"> {ERROR} {CROSS} Failed to create project")
            console.print(
                f'''> Reason for failure {SAD_SMILEY}:- " {RED_START}{json_response[DATA]['error']}{RED_END} "'''
            )
    return json_response


async def delete_project(project_id: Text) -> Dict[Text, Any]:
    console.print(f"> {INFO} {BIN} Deleting project with id: {project_id}")
    payload = {PROJECT_ID: project_id}
    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()
    async with get_async_http_session().delete(
        url=f"{neuralspace_url()}/{DELETE_PROJECT_URL}",
        data=json.dumps(payload),
        headers=HEADERS,
    ) as response:
        json_response = await response.json(encoding="utf-8")
        if is_success_status(response.status):
            console.print(f"> {INFO} {GREEN_TICK} Successfully deleted project")
            console.print(
                f"{FAST_FORWARD} To create the project:  {DARK_ORANGE_START}{CREATE_PROJECT_COMMAND}{DARK_ORANGE_END}"
            )
        else:
            console.print(f"> {ERROR} {CROSS} Failed to delete projects")
            console.print(
                f"> Reason for failure {SAD_SMILEY}:- {RED_START}{json_response[MESSAGE]}{RED_END}"
            )
    return json_response


def print_projects_table(projects: Dict[Text, Any], verbose: bool):
    table = Table(show_header=True, header_style="bold #c47900", show_lines=True)
    table.add_column("Project Name")
    table.add_column("Project ID")
    if verbose:
        table.add_column("Languages")
        table.add_column("Number of Examples")
        table.add_column("Number of Intents")
        table.add_column("Number of Models")
    for data in projects[DATA][PROJECTS]:
        args = [data[PROJECT_NAME], data[PROJECT_ID]]
        if verbose:
            args += [
                ", ".join(data[LANGUAGE]),
                str(data[NUMBER_OF_EXAMPLES]),
                str(data[NUMBER_OF_INTENTS]),
                str(data[NUMBER_OF_MODELS]),
            ]
        table.add_row(*args)
    console.print(table)


async def list_projects(
    search: Text, page_size: int, page_number: int, languages: List[Text], verbose: bool
) -> Dict[Text, Any]:
    payload = {
        SEARCH: search,
        PAGE_NUMBER: page_number,
        PAGE_SIZE: page_size,
        LANGUAGES: languages,
    }
    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()
    async with get_async_http_session().post(
        url=f"{neuralspace_url()}/{LIST_PROJECTS_URL}",
        data=json.dumps(payload),
        headers=HEADERS,
    ) as response:
        json_response = await response.json(encoding="utf-8")
        if is_success_status(response.status):
            console.print(
                f"> {INFO} {BOOK} Your projects for Page {page_number} "
                f"with Page Size: {page_size}"
            )
            print_projects_table(json_response, verbose)
            console.print(
                f"{FAST_FORWARD} To upload your dataset: {DARK_ORANGE_START}{UPLOAD_DATASET_COMMAND}{DARK_ORANGE_END}"
            )
        else:
            console.print(f"> {ERROR} {CROSS} Failed to list projects")
            console.print(
                f'''> Reason for failure {SAD_SMILEY}: " {RED_START}{json_response[MESSAGE]}{RED_END} "'''
            )
    return json_response


def print_examples_table(examples: Dict[Text, Any], verbose: bool = False):
    table = Table(show_header=True, header_style="bold #c47900", show_lines=True)
    table.add_column("Example ID")
    table.add_column("Text")
    if verbose:
        table.add_column("Intent")
        table.add_column("N Entities", style="#c47900")

    console.print(
        f"> {INFO} {NUMBERS_IN_SQUARE} Total Examples Count: {examples[DATA][COUNT]}"
    )
    for data in examples[DATA][EXAMPLES]:
        marked_sentence = ""
        start_index = []
        end_index = []
        for i, entities in enumerate(data[ENTITIES]):
            start_index.append(entities[START])
            end_index.append(entities[END])
        for idx, character in enumerate(data[TEXT]):
            if idx in start_index:
                marked_sentence += "[bold green]"
            elif idx in end_index:
                marked_sentence += "[/bold green]"
            marked_sentence += character
        args = [data[EXAMPLE_ID], marked_sentence]
        if verbose:
            args += [data[INTENT], str(len(data[ENTITIES]))]
        table.add_row(*args)

    console.print(table)


async def list_examples(
    project_id: Text,
    language: Text,
    prepared: bool,
    type: Text,
    intent: Text,
    page_number: int,
    page_size: int,
    verbose: bool = False,
) -> Dict[Text, Any]:
    console.print(
        f"> {INFO} {DOWN_ARROW}️ Fetching Examples with filter: \n"
        f"> {INFO} {HASH} {BOLD_START}Project ID:{BOLD_END} {ORANGE_START}{project_id}{ORANGE_END}\n"
        f"> {INFO} {OM} Language: {language}\n"
        f"> {INFO} {SOUP} Prepared: {prepared}\n"
        f"> {INFO} {PIN} type: {type}"
    )
    payload = {
        FILTER: {
            PROJECT_ID: project_id,
            LANGUAGE: language,
            PREPARED: prepared,
            TYPE: type,
        },
        PAGE_NUMBER: page_number,
        PAGE_SIZE: page_size,
    }
    if intent:
        payload[FILTER][INTENT] = intent

    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()
    async with get_async_http_session().post(
        url=f"{neuralspace_url()}/{LIST_EXAMPLES_URL}",
        data=json.dumps(payload),
        headers=HEADERS,
    ) as response:
        json_response = await response.json(encoding="utf-8")
        if is_success_status(response.status):
            print_examples_table(json_response, verbose)
            console.print(
                f"{FAST_FORWARD} To train the model: {DARK_ORANGE_START}{TRAIN_MODEL_COMMAND}{DARK_ORANGE_END}"
            )
            console.print(
                f"{RED_START}{PEN_AND_PAPER}NOTE: To train a model in a project, the project must have minimum"
                f" [orange4]2[/orange4] intent and every intent must atleast have{RED_END} "
                f"[orange4]10[/orange4] {RED_START}training examples{RED_END}"
            )
        else:
            console.print(f"> {ERROR} {CROSS} Failed to list examples")
            console.print(
                f'''> Reason for failure {SAD_SMILEY}: " {RED_START}{json_response[MESSAGE]}{RED_END} "'''
            )

    return json_response


def get_training_status_colour(status: Text) -> Text:
    if status == COMPLETED:
        return C_COMPLETED
    if status == TRAINING:
        return C_TRAINING
    elif status == FAILED:
        return C_FAILED
    elif status == TIMED_OUT:
        return C_TIMED_OUT
    elif status == DEAD:
        return C_DEAD
    elif status == INITIATED:
        return C_INITIATED
    elif status == QUEUED:
        return C_QUEUED
    elif status == SAVED:
        return C_COMPLETED


def print_models_table(models: Dict[Text, Any], verbose: bool):
    table = Table(show_header=True, header_style="bold #c47900", show_lines=True)
    table.add_column("Model ID")
    table.add_column("Model Name")
    if verbose:
        table.add_column("Training Status")
        table.add_column("Replicas")
        table.add_column("Intent Acc")
        table.add_column("Entity Acc")
        table.add_column("Training Time (sec)")
        table.add_column("Last Updated")
        table.add_column("Training Message")

    console.print(
        f"> {INFO} {NUMBERS_IN_SQUARE} Total Models Count: {models[DATA][COUNT]}"
    )
    for data in models[DATA][MODELS]:
        args = [data[MODEL_ID], data[MODEL_NAME]]
        if verbose:
            args += [
                f"{get_training_status_colour(data[TRAINING_STATUS])} {data[TRAINING_STATUS]}",
                str(data[REPLICAS]),
                "{:.3f}".format(
                    data[METRICS][INTENT_CLASSIFIER_METRICS][INTENT_ACCURACY]
                )
                if data[TRAINING_STATUS] == COMPLETED
                else "0.0",
                "{:.3f}".format(data[METRICS][NER_METRICS][ENTITY_ACC])
                if data[TRAINING_STATUS] == COMPLETED
                else "0.0",
                str(data[TRAINING_TIME])
                if data[TRAINING_STATUS] == COMPLETED
                else "0.0",
                str(data[LAST_STATUS_UPDATED]),
                data[MESSAGE],
            ]
        table.add_row(*args)
    console.print(table)


async def list_models(
    project_id: Text,
    language: Text,
    training_status: List[Text],
    page_number: int,
    page_size: int,
    verbose: bool,
) -> Dict[Text, Any]:
    console.print(
        f"> {INFO} {DOWN_ARROW}️ Fetching models with filter: \n"
        f"> {INFO} {FINGER_RIGHT} Project ID: {project_id}\n"
        f"> {INFO} {PERSON_TAKING} Language: {language}\n"
        f"> {INFO} {PERSON_DUMBELL}️ Training Statuses: {training_status}"
    )
    payload = {
        FILTER: {PROJECT_ID: project_id, LANGUAGE: language},
        PAGE_NUMBER: page_number,
        PAGE_SIZE: page_size,
    }
    if training_status:
        payload[FILTER][TRAINING_STATUS] = training_status

    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()
    async with get_async_http_session().post(
        url=f"{neuralspace_url()}/{LIST_MODELS_URL}",
        data=json.dumps(payload),
        headers=HEADERS,
    ) as response:
        json_response = await response.json(encoding="utf-8")
        if is_success_status(response.status):
            print_models_table(json_response, verbose)
            console.print(
                f"{FAST_FORWARD} To deploy the model: {DARK_ORANGE_START}{DEPLOY_MODEL_COMMAND}{DARK_ORANGE_START}"
            )
        else:
            console.print(f"> {ERROR} {CROSS} Failed to list models")
            console.print(
                f'''> Reason for failure {SAD_SMILEY}: " {RED_START}{json_response[MESSAGE]}{RED_END} "'''
            )
    return json_response


async def delete_examples(example_ids: List[Text]) -> Dict[Text, Any]:
    console.print(f"> {INFO} {BIN} Deleting Example with id: {example_ids}")
    payload = {EXAMPLE_ID: example_ids}
    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()
    async with get_async_http_session().delete(
        url=f"{neuralspace_url()}/{DELETE_EXAMPLE_URL}",
        data=json.dumps(payload),
        headers=HEADERS,
    ) as response:
        json_response = await response.json(encoding="utf-8")
        if is_success_status(response.status):
            console.print(f"> {INFO} {GREEN_TICK} Successfully deleted example!")
        else:
            console.print(f"> {ERROR} {CROSS} Failed to delete examples")
            console.print(
                f'''> Reason for failure {SAD_SMILEY}: " {RED_START}{json_response[MESSAGE]}{RED_END} "'''
            )
    return json_response


async def upload_dataset(
    nlu_data: List[Dict[Text, Text]],
    project_id: Text,
    language: Text,
    skip_first: int = 0,
    ignore_errors: bool = False,
) -> List[Dict[Text, Any]]:
    responses = []
    error_examples = []
    console.print(
        f"> {INFO} Uploading {len(nlu_data) - skip_first} "
        f"examples for project {project_id} and language {language}"
    )
    console.print(f"> {INFO} Skipping first {skip_first} examples")
    Total_number_examples = len(nlu_data[skip_first:])
    current_example_number = 0
    progress_bar = Progress(
        SpinnerColumn(),
        TextColumn(
            "[orange3]Uploading...[/orange3]"
            " [dark_green]{task.completed}[/dark_green]/[dark_green]{task.total}[/dark_green]"
        ),
        BarColumn(bar_width=50),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
        CustomisedTransferSpeedColumn(),
        "[orange3][progress.description]{task.description}[/orange3]",
    )
    task = progress_bar.add_task(description="", total=Total_number_examples)
    progress_bar.update(task)
    animation_tracker = 1
    for chunk_id, example in enumerate(nlu_data):
        progress_bar.start()
        current_example_number += 1
        batch = {PROJECT_ID: project_id, LANGUAGE: language, EXAMPLE: example}
        HEADERS = copy(COMMON_HEADERS)
        HEADERS[AUTHORIZATION] = get_auth_token()
        async with get_async_http_session().post(
            url=f"{neuralspace_url()}/{CREATE_EXAMPLE_URL}",
            data=json.dumps(batch, ensure_ascii=False),
            headers=HEADERS,
        ) as response:
            json_response = await response.json(encoding="utf-8")
            if is_success_status(response.status):
                if current_example_number % 3 == 0:
                    if animation_tracker == 1:
                        progress_bar.update(task_id=task, description="🏃")
                        animation_tracker = 2
                    elif animation_tracker == 2:
                        progress_bar.update(task_id=task, description="🚶")
                        animation_tracker = 3
                    elif animation_tracker == 3:
                        progress_bar.update(task_id=task, description="🏃")
                        animation_tracker = 1
                responses.append(json_response)
                progress_bar.update(task_id=task, completed=current_example_number)
            else:
                console.print(
                    f"> {ERROR} {CROSS} Failed to upload example with text "
                    f"{DARK_ORANGE_START}{example['text']}{DARK_ORANGE_END}"
                )

                console.print(
                    f"> Failed on example: \n{json.dumps(example, indent=4, ensure_ascii=False)}"
                )
                console.print(
                    f'''> Reason for failure {SAD_SMILEY}: " {RED_START}{json_response[MESSAGE]}{RED_END} "'''
                )
                error_examples.append(example)
                if ignore_errors:
                    continue
                else:
                    break
    console.print(f"\n> {INFO} {GREEN_TICK} Uploaded {len(responses)} examples")
    console.print(f"> {INFO} {CROSS} Failed on {len(error_examples)} examples")
    with open("failed_examples.json", "w") as f:
        json.dump(error_examples, f, ensure_ascii=False)
        console.print(
            f"> {INFO} {WRITING} Writing failed examples into failed_examples.json"
        )
    console.print(
        f"To train your model: {DARK_ORANGE_START}{TRAIN_MODEL_COMMAND}{DARK_ORANGE_END}"
    )
    return responses


async def wait_till_training_completes(
    model_id: Text, wait: bool, wait_interval: int
) -> Dict[Text, Any]:
    json_response = None
    if wait:
        payload = {
            MODEL_ID: model_id,
        }
        HEADERS = copy(COMMON_HEADERS)
        HEADERS[AUTHORIZATION] = get_auth_token()
        console.print(
            f"> {INFO} {SAND_CLOCK} Waiting for model to "
            f"get trained; model id: {model_id}"
        )
        current_status = ""
        with console.status("...") as status:
            while True:
                async with get_async_http_session().get(
                    url=f"{neuralspace_url()}/{SINGLE_MODEL_DETAILS_URL}",
                    params=payload,
                    headers=HEADERS,
                ) as response:
                    json_response = await response.json(encoding="utf-8")
                    if is_success_status(response.status):
                        current_status = json_response[DATA][TRAINING_STATUS]
                        if (
                            json_response[DATA][TRAINING_STATUS] == COMPLETED
                            or json_response[DATA][TRAINING_STATUS] == FAILED
                            or json_response[DATA][TRAINING_STATUS] == TIMED_OUT
                            or json_response[DATA][TRAINING_STATUS] == DEAD
                        ):
                            if json_response[DATA][TRAINING_STATUS] == COMPLETED:
                                console.print(
                                    f"{FAST_FORWARD} To deploy your model on Neuralspace platform: "
                                    f"{DARK_ORANGE_START}{DEPLOY_MODEL_COMMAND}{DARK_ORANGE_END}"
                                )
                            if json_response[DATA][TRAINING_STATUS] == FAILED:
                                console.print(
                                    f'''> Reason for failure {SAD_SMILEY}: " {RED_START}{json_response[DATA][MESSAGE]}{RED_END}\
                                     "'''
                                )
                            break
                    else:
                        console.print(f"> {ERROR} Failed to fetch model details")
                        console.print(
                            f'''> Reason for failure {SAD_SMILEY}:
                            " {RED_START}{json_response[MESSAGE]}{RED_END} "'''
                        )
                        break
                    status.update(f"Model is {current_status} {PERSON_STANDING}")
                    await sleep(wait_interval)
                    status.update(f"Model is {current_status} {PERSON_DUMBELL}")
            console.print(
                f"> {INFO} "
                f"{get_training_status_colour(json_response[DATA][TRAINING_STATUS])} "
                f"Training status: {json_response[DATA][TRAINING_STATUS]}"
            )
    return json_response


async def train_model(
    project_id: Text,
    language: Text,
    model_name: Text,
    wait: bool = True,
    wait_time: int = 1,
) -> Tuple[Dict[Text, Any], Dict[Text, Any]]:
    console.print(
        f"> {INFO} Queuing training job for: \n"
        f"> {INFO} Project ID: {project_id}\n"
        f"> {INFO} Language: {language}\n"
        f"> {INFO} Model Name: {model_name}"
    )
    payload = {PROJECT_ID: project_id, LANGUAGE: language, MODEL_NAME: model_name}
    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()

    async with get_async_http_session().post(
        url=f"{neuralspace_url()}/{TRAIN_MODEL_URL}",
        data=json.dumps(payload),
        headers=HEADERS,
    ) as response:
        json_response = await response.json(encoding="utf-8")
        if is_success_status(response.status):
            console.print("> {INFO} Training job queued successfully")
            model_id = json_response[DATA][MODEL_ID_key]
            last_model_status = await wait_till_training_completes(
                model_id, wait, wait_time
            )
        else:
            console.print(f"> {ERROR} Failed to queue training job")
            console.print(f"> {ERROR} {json_response[MESSAGE]}")
            last_model_status = None
    return json_response, last_model_status


async def delete_models(model_id: Text) -> Dict[Text, Any]:
    console.print(f"> {INFO} {BIN} Deleting model with id: {model_id}")
    payload = {MODEL_ID: model_id}
    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()
    async with get_async_http_session().delete(
        url=f"{neuralspace_url()}/{DELETE_MODELS_URL}",
        data=json.dumps(payload),
        headers=HEADERS,
    ) as response:
        json_response = await response.json(encoding="utf-8")
        if is_success_status(response.status):
            console.print(f"> {INFO} {GREEN_TICK} Successfully deleted model")
            console.print(
                f"{FAST_FORWARD} To upload the dataset: {DARK_ORANGE_START}{UPLOAD_DATASET_COMMAND}{DARK_ORANGE_END}"
            )
        else:
            console.print(f"> {ERROR} {CROSS} Failed to delete models")
            console.print(
                f'''> Reason for failure {SAD_SMILEY}: " {RED_START}{json_response[MESSAGE]}{RED_END} "'''
            )
    return json_response


async def deploy(model_id: Text, n_replicas: int) -> Dict[Text, Any]:
    console.print(
        f"> {INFO} {ARROW_UP}️ Deploying: Model ID: {model_id}; Replicas: {n_replicas};"
    )
    payload = {MODEL_ID: model_id, N_REPLICAS: n_replicas}
    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()

    async with get_async_http_session().post(
        url=f"{neuralspace_url()}/{DEPLOY_MODEL_URL}",
        data=json.dumps(payload),
        headers=HEADERS,
    ) as response:
        json_response = await response.json(encoding="utf-8")
        if is_success_status(response.status):
            console.print(f"> {INFO} {GREEN_TICK} Model deployed successfully")
            console.print(
                f"{FAST_FORWARD} To parse the model: {DARK_ORANGE_START}{PARSE_MODEL_COMMAND}{DARK_ORANGE_END}"
            )
        else:
            console.print(f"> {ERROR} {CROSS} Failed to deploy model")
            console.print(
                f'''> Reason for failure {SAD_SMILEY}: " {RED_START}{json_response[MESSAGE]}{RED_END} "'''
            )
    return json_response


def print_nlu_response(nlu_response: Dict[Text, Any], response_time: float):
    table = Table(show_header=True, header_style="bold #c47900", show_lines=True)
    table.add_column("Text")
    table.add_column("Intent")
    table.add_column("Intent Confidence")
    table.add_column("Response Time (sec)")
    table.add_row(
        nlu_response[DATA][TEXT],
        nlu_response[DATA][INTENT][NAME],
        str(nlu_response[DATA][INTENT][CONFIDENCE]),
        str(response_time / 1000),
    )
    console.print(table)
    intent_ranking_table = Table(
        show_header=True, header_style="bold #c47900", show_lines=True
    )
    intent_ranking_table.add_column("Intent")
    intent_ranking_table.add_column("Confidence")

    for row in nlu_response[DATA][INTENT_RANKING]:
        intent_ranking_table.add_row(
            row["name"],
            str(row["confidence"]),
        )
    console.print(f"> {INFO} Intent Ranking")
    console.print(intent_ranking_table)
    formatted_entities = []
    for e in nlu_response[DATA][ENTITIES]:
        e[START_INDEX] = e[START]
        e[END_INDEX] = e[END]
        e[TYPE] = e[ENTITY]
        formatted_entities.append(e)
    print_ner_response(formatted_entities, nlu_response[DATA][TEXT])


async def parse(model_id: Text, input_text: Text) -> Dict[Text, Any]:
    console.print(
        f"> {INFO} {PEN_AND_PAPER} Parsing text: {input_text}, using Model ID: {model_id}"
    )
    payload = {MODEL_ID: model_id, TEXT: input_text}
    HEADERS = copy(COMMON_HEADERS)
    HEADERS[AUTHORIZATION] = get_auth_token()

    start = datetime.now()
    async with get_async_http_session().post(
        url=f"{neuralspace_url()}/{PARSE_URL}",
        data=json.dumps(payload, ensure_ascii=False),
        headers=HEADERS,
    ) as response:
        end = datetime.now()
        response_time = (end - start).microseconds
        json_response = await response.json(encoding="utf-8")
        if is_success_status(response.status):
            console.print(f"> {INFO} {GREEN_TICK} Successfully parsed text")
            print_nlu_response(json_response, response_time)
        else:
            console.print(f"> {ERROR} {CROSS} Failed to parse model")
            console.print(
                f'''> Reason for failure {SAD_SMILEY}: " {RED_START}{json_response[MESSAGE]}{RED_END} "'''
            )
    return json_response
