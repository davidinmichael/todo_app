import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Todo extends StatefulWidget {
  const Todo({super.key});

  @override
  State<Todo> createState() => _TodoState();
}

class _TodoState extends State<Todo> {
  List todos = [];

  void getTodo() async {
    const url = "http://127.0.0.1:8000/todo";
    final uri = Uri.parse(url);
    final response = await http.get(uri);
    final todo = jsonDecode(response.body);
    print(todo);

    setState(() {
      todos = todo;
    });
  }

  @override
  void initState() {
    super.initState();
    getTodo();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "Todo Lists",
      home: Scaffold(
        body: ListView.builder(
          itemCount: todos.length,
          itemBuilder: ((context, index) {
            final todo = todos[index];
            return Padding(
              padding: const EdgeInsets.all(20.0),
              child: Card(
                elevation: 10,
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: ListTile(
                    title: Text(todo["title"]),
                    leading: Checkbox(
                      checkColor: Colors.orange,
                      fillColor: MaterialStateProperty.all(Colors.black),
                      value: todo["completed"],
                      onChanged: (bool? value) {
                        setState(() {
                          todo["completed"] = value!;
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
      ),
    );
  }
}
