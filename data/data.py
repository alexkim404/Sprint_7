BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

# API
API_ENDPOINTS = {
    "create_courier": f"{BASE_URL}/courier",
    "login_courier": f"{BASE_URL}/courier/login",
    "delete_created_courier": f"{BASE_URL}/courier/{{id}}",
    "list_orders": f"{BASE_URL}/orders",
    "create_order": f"{BASE_URL}/orders",
    "accept_order": f"{BASE_URL}/orders/accept",
    "track_order": f"{BASE_URL}/orders/track",
    "cancel_order": f"{BASE_URL}/orders/cancel",
    "finish_order": f"{BASE_URL}/orders/finish",
}

# Ожидаемые ответы
EXPECTED_RESPONSES = {
    "create_courier_success_code": 201,
    "create_courier_success_response": {"ok": True},
    "create_courier_missing_data_code": 400,
    "create_courier_missing_data_message": "Недостаточно данных для создания учетной записи",
    "create_courier_duplicate_code": 409,
    "create_courier_duplicate_message": "Этот логин уже используется. Попробуйте другой.",

    "login_courier_success_code": 200,
    "login_courier_success_response": {"id": 12345},
    "login_courier_missing_data_code": 400,
    "login_courier_missing_data_message": "Недостаточно данных для входа",
    "login_courier_invalid_code": 404,
    "login_courier_invalid_message": "Учетная запись не найдена",
    "login_courier_missing_field_code": 504,
    "login_courier_missing_field_message": "Service unavailable",

    "delete_courier_success_code": 200,
    "delete_courier_success_response": {"ok": True},
    "delete_courier_missing_data_code": 400,
    "delete_courier_missing_data_message": "Недостаточно данных для удаления курьера",
    "delete_courier_not_found_code": 404,
    "delete_courier_not_found_message": "Курьера с таким id нет.",

    "get_courier_orders_count_success_code": 200,
    "get_courier_orders_count_success_response": {"id": "123456", "ordersCount": "100500"},
    "get_courier_orders_count_missing_data_code": 400,
    "get_courier_orders_count_missing_data_message": "Недостаточно данных для поиска",
    "get_courier_orders_count_not_found_code": 404,
    "get_courier_orders_count_not_found_message": "Курьер не найден",

    "finish_order_success_code": 200,
    "finish_order_success_response": {"ok": True},
    "finish_order_missing_data_code": 400,
    "finish_order_missing_data_message": "Недостаточно данных для поиска",
    "finish_order_not_found_order_code": 404,
    "finish_order_not_found_order_message": "Заказа с таким id не существует",
    "finish_order_not_found_courier_code": 404,
    "finish_order_not_found_courier_message": "Курьера с таким id не существует",
    "finish_order_conflict_code": 409,
    "finish_order_conflict_message": "Этот заказ нельзя завершить",

    "cancel_order_success_code": 200,
    "cancel_order_success_response": {"ok": True},
    "cancel_order_missing_data_code": 400,
    "cancel_order_missing_data_message": "Недостаточно данных для поиска",
    "cancel_order_not_found_code": 404,
    "cancel_order_not_found_message": "Заказ не найден",
    "cancel_order_conflict_code": 409,
    "cancel_order_conflict_message": "Этот заказ уже в работе",

    "get_orders_list_success_code": 200,
    "get_orders_list_success_response": {"orders": list},

    "get_orders_list_courier_not_found_code": 404,
    "get_orders_list_courier_not_found_message": "Курьер с идентификатором {} не найден",
    "get_orders_list_bad_request_code": 500,
    "get_orders_list_bad_request_message": "Некорректные параметры запроса",

    "get_order_by_track_success_code": 200,
    "get_order_by_track_success_response": {"order": dict},
    "get_order_by_track_missing_data_code": 400,
    "get_order_by_track_missing_data_message": "Недостаточно данных для поиска",
    "get_order_by_track_not_found_code": 404,
    "get_order_by_track_not_found_message": "Заказ не найден",

    "accept_order_success_code": 200,
    "accept_order_success_response": {"ok": True},
    "accept_order_missing_data_code": 400,
    "accept_order_missing_data_message": "Недостаточно данных для поиска",
    "accept_order_not_found_order_code": 404,
    "accept_order_not_found_order_message": "Заказа с таким id не существует",
    "accept_order_not_found_courier_code": 404,
    "accept_order_not_found_courier_message": "Курьера с таким id не существует",
    "accept_order_conflict_code": 409,
    "accept_order_conflict_message": "Этот заказ уже в работе",
    "accept_order_conflict_missing_data_code": 400,
    "accept_order_conflict_missing_data_message": "Недостаточно данных для поиска",

    "create_order_success_code": 201,
    "create_order_success_response": {"track": 124124},
    "create_order_missing_field_code": 400,
    "create_order_missing_field_message": "Не заполнено обязательное поле {field}",
    "create_order_empty_field_code": 400,
    "create_order_empty_field_message": "Поле {field} не может быть пустым",
    "create_order_server_error_code": 500,
    "create_order_server_error_message": "invalid input syntax for type integer",
    "create_order_server_error_message_date": "invalid input syntax for type timestamp with time zone",

    "ping_server_success_code": 200,
    "ping_server_success_message": "pong",

    "search_stations_success_code": 200,
    "search_stations_success_message": "OK"
}

ORDER_COLORS = ["BLACK", "GREY"]

ORDER_STATUSES = {
    "CREATED": 0,
    "ACCEPTED": 1,
    "COMPLETED": 2,
    "CANCELLED": -1
}