# Project_template

Это шаблон для решения проектной работы. Структура этого файла повторяет структуру заданий. Заполняйте его по мере работы над решением.

# Задание 1. Анализ и планирование
Текущее приложение компании позволяет управлять отоплением в доме и проверять температуру.
Язык программирования: Go
База данных: PostgreSQL
Архитектура: Монолитная, все компоненты системы (обработка запросов, бизнес-логика, работа с данными) находятся в рамках одного приложения.
Взаимодействие: Синхронное, запросы обрабатываются последовательно.
Масштабируемость: Ограничена, так как монолит сложно масштабировать по частям.
Развертывание: Требует остановки всего приложения.
REST API для внешних запросов(temperature-api сервис).

### 1. Описание функциональности монолитного приложения

**Управление отоплением:**

- Пользователи могут включать/отключать отопление в доме
- Пользователи могут задавать температуру в доме
- 
- Система поддерживает управление датчиками(создание, обновление, удаление, 
  получение информации о всех датчиках и получение информации конкретного датчика по id)
- Система поддерживает обновление значений датчиков(температуру и статус)


**Мониторинг температуры:**

- Пользователи могут получать данные о температуре в доме
- Система поддерживает получение информации о температуре в доме по id датчика

### 2. Анализ архитектуры монолитного приложения

Язык программирования: Go (основная бизнес-логика), REST API для внешних запросов.

База данных: PostgreSQL (одна таблица sensors для датчиков).

Взаимодействие компонентов: SensorsHandler обрабатывает HTTP-запросы и вызывает сервисный слой (TemperatureService и RepositoryLayer).

TemperatureService получает данные о температуре через REST-запросы к Python-сервису TemperatureApp.

RepositoryLayer выполняет CRUD-операции с PostgreSQL.

Особенности:

Монолит объединяет управление сенсорами и логику работы с температурой.
Взаимодействие с внешним Python-сервисом выполняется синхронно через REST.

### 3. Определение доменов и границы контекстов
Sensors (Сенсоры)
Описание: Управление сенсорами, CRUD операции, получение текущего состояния.
Компоненты:
SensorsHandler — HTTP обработчик запросов к сенсорам
RepositoryLayer — слой доступа к базе данных (технический компонент, поддержка домена)
Database — хранение информации о сенсорах (инфраструктура)

Temperature (Температура / Мониторинг)
Описание: Получение актуальных данных о температуре с устройств.
Компоненты:
TemperatureService — бизнес-логика по обработке температурных данных

### **4. Проблемы монолитного решения**
Масштабирование: нельзя масштабировать отдельно обработку сенсоров или температурные вычисления.
Надёжность: сбой одного сервиса поломает все, невозможно будет не читать сенсоры, не получать температуру.


### 5. Визуализация контекста системы — диаграмма С4

Добавьте сюда диаграмму контекста в модели C4.

Чтобы добавить ссылку в файл Readme.md, нужно использовать синтаксис Markdown. Это делают так:

```markdown
[Монолит- Диаграмма контекста](apps/diagrams/oldmonolith/context/Context.puml)
```

```markdown
[Монолит- Диаграмма контейнеров](apps/diagrams/oldmonolith/container/Container.puml)
```
```markdown
[Монолит- Диаграмма компонента-smarthome](apps/diagrams/oldmonolith/component/Component-smarthome-api.puml)
```
```markdown
[Монолит- Диаграмма компонента-smarthome](apps/diagrams/oldmonolith/component/Component-temperature-api.puml)
```

# Задание 2. Проектирование микросервисной архитектуры

В этом задании вам нужно предоставить только диаграммы в модели C4. Мы не просим вас отдельно описывать получившиеся микросервисы и то, как вы определили взаимодействия между компонентами To-Be системы. Если вы правильно подготовите диаграммы C4, они и так это покажут.

**Диаграмма контейнеров (Containers)**
```markdown
[Диаграмма контекста](apps/diagrams/warmhouse/container/Container.puml)
```

**Диаграмма компонентов (Components)**

```markdown
[Диаграмма компонента-core сервис умного дома](apps/diagrams/warmhouse/component/Component-smarthome-core.puml)
```
```markdown
[Диаграмма компонента-сервис управления отоплением](apps/diagrams/warmhouse/component/Component-heating-service.puml)
```
```markdown
[Диаграмма компонента-сервис управления воротами](apps/diagrams/warmhouse/component/Component-gate-service.puml)
```
```markdown
[Диаграмма компонента-сервис управления освещением](apps/diagrams/warmhouse/component/Component-lighting-service.puml)
```
```markdown
[Диаграмма компонента-сервис управления камерами](apps/diagrams/warmhouse/component/Component-camera-service.puml)
```
```markdown
[Диаграмма компонента-сервис аутентификации](apps/diagrams/warmhouse/component/Component-auth-service.puml)
```


**Диаграмма кода (Code)**

```markdown
[Диаграмма кода-сервис управления воротами](apps/diagrams/warmhouse/code/Code-gate-service.puml)
```

# Задание 3. Разработка ER-диаграммы

Добавьте сюда ER-диаграмму. Она должна отражать ключевые сущности системы, их атрибуты и тип связей между ними.

# Задание 4. Создание и документирование API

### 1. Тип API

В качестве контракта будет использоваться Openapi, из самых распостраненных типов Api для rest запросов.
Исключением является camera-service, для него будет использоваться также proto формат для grpc запроса, 
т.к. у нас в данном сервисе будет использоваться grpc-streaming.

### 2. Документация API

Здесь приложите ссылки на документацию API для микросервисов, которые вы спроектировали в первой части проектной работы. Для документирования используйте Swagger/OpenAPI или AsyncAPI.

```markdown
[Openapi-сервис аутентификации](apps/api//openapi-auth-service.yaml)
```
```markdown
[Openapi-gateway сервис](apps/api/openapi-gateway-service.yaml)
```
```markdown
[Openapi-сервис работы камер](apps/api/openapi-camera-service.yaml)
```
```markdown
[Openapi-сервис работы отопления](apps/api/openapi-heating-service.yaml)
```
```markdown
[Openapi-сервис работы освещения](apps/api/openapi-lighting-service.yaml)
```
```markdown
[Openapi-сервис работы ворот](apps/api/openapi-gate-service.yaml)
```
```markdown
[Openapi-core сервис умного дома](apps/api/openapi-smarthome-core-service.yaml)
```
```markdown
[Proto-сервис работы камер](apps/api/proto/camera-service.proto)
```


# Задание 5. Работа с docker и docker-compose (DONE)

Перейдите в apps.

Там находится приложение-монолит для работы с датчиками температуры. В README.md описано как запустить решение.

Вам нужно:

1) сделать простое приложение temperature-api на любом удобном для вас языке программирования, которое при запросе /temperature?location= будет отдавать рандомное значение температуры.

Locations - название комнаты, sensorId - идентификатор названия комнаты

```
	// If no location is provided, use a default based on sensor ID
	if location == "" {
		switch sensorID {
		case "1":
			location = "Living Room"
		case "2":
			location = "Bedroom"
		case "3":
			location = "Kitchen"
		default:
			location = "Unknown"
		}
	}

	// If no sensor ID is provided, generate one based on location
	if sensorID == "" {
		switch location {
		case "Living Room":
			sensorID = "1"
		case "Bedroom":
			sensorID = "2"
		case "Kitchen":
			sensorID = "3"
		default:
			sensorID = "0"
		}
	}
```

2) Приложение следует упаковать в Docker и добавить в docker-compose. Порт по умолчанию должен быть 8081

3) Кроме того для smart_home приложения требуется база данных - добавьте в docker-compose файл настройки для запуска postgres с указанием скрипта инициализации ./smart_home/init.sql

Для проверки можно использовать Postman коллекцию smarthome-api.postman_collection.json и вызвать:

- Create Sensor
- Get All Sensors

Должно при каждом вызове отображаться разное значение температуры

Ревьюер будет проверять точно так же.


