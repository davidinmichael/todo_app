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
    print("Button Pressed");
    const url = "https://davidinmichael.pythonanywhere.com/blog/";
    print("Link Loading");
    final uri = Uri.parse(url);
    final response = await http.get(uri);
    final todo = jsonDecode(response.body);
    print("Button Done");
    print(response.statusCode);

    setState(() {
      todos = todo["results"];
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
            final todoTitle = todo["title"];
            final todoContent = todo["content"];
            return Padding(
              padding: const EdgeInsets.all(20.0),
              child: Card(
                elevation: 10,
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: ListTile(
                    title: Text(todoTitle),
                    subtitle: Text(todoContent),
                    leading: IconButton(
                      icon: Icon(Icons.more_vert),
                    onPressed: () {},
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
