import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Todo extends StatefulWidget {
  const Todo({Key? key}) : super(key: key);

  @override
  State<Todo> createState() => _TodoState();
}

class _TodoState extends State<Todo> {
  List<Map<String, dynamic>> todos = [];

  void getTodo() async {
    print("Button Pressed");
    const url = "http://127.0.0.1:8000/todo/";
    print("Link Loading");
    final uri = Uri.parse(url);
    final response = await http.get(uri);
    final todoList = jsonDecode(response.body);
    print("Button Done");
    print(response.statusCode);

    setState(() {
      todos = List.from(todoList);
    });
  }

  Future<void> updateTodoCompletion(int todoId, bool completed) async {
    final url =
        "http://127.0.0.1:8000/edit/$todoId/"; // Use the correct endpoint for updating a specific todo
    final uri = Uri.parse(url);
    final headers = {"content-type": "application/json"};
    final body = jsonEncode({"completed": completed});

    final response = await http.put(uri, headers: headers, body: body);

    if (response.statusCode == 202) {
      print("Todo updated successfully");
    } else {
      print("Failed to update todo");
    }
  }

  @override
  void initState() {
    super.initState();
    getTodo();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView.builder(
        itemCount: todos.length,
        itemBuilder: ((context, index) {
          final todo = todos[index];
          final title = todo["title"];
          final dateAdded = todo["date_added"];
          bool completed = todo["completed"];
          int todoId = todo["id"];

          return Padding(
            padding: const EdgeInsets.all(10.0),
            child: Card(
              elevation: 10,
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: ListTile(
                  title: Text(title),
                  subtitle: Text(dateAdded),
                  trailing: Checkbox(
                    checkColor: Colors.red,
                    value: completed,
                    onChanged: (bool? value) {
                      setState(() {
                        completed = value!;
                        updateTodoCompletion(todoId,
                            completed); // Call the updateTodoCompletion function
                      });
                    },
                  ),
                ),
              ),
            ),
          );
        }),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
      floatingActionButton: FloatingActionButton(
        onPressed: getTodo,
        child: Icon(Icons.add),
      ),
    );
  }
  void addTodo() {
    
  }
}
