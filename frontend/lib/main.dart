import 'package:flutter/cupertino.dart';

void main() => runApp(const TabScaffoldApp());

class TabScaffoldApp extends StatelessWidget {
  const TabScaffoldApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const CupertinoApp(
      theme: CupertinoThemeData(brightness: Brightness.light),
      home: TabScaffoldWidget(),
    );
  }
}

class TabScaffoldWidget extends StatefulWidget {
  const TabScaffoldWidget({super.key});

  @override
  State<TabScaffoldWidget> createState() => TabScaffoldState();
}

class TabScaffoldState extends State<TabScaffoldWidget> {
  @override
  Widget build(BuildContext context) {
    return CupertinoTabScaffold(
      tabBar: CupertinoTabBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.map),
            label: 'Mapa',
          ),
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.search_circle_fill),
            label: 'Hledání spojení',
          ),
        ],
      ),
      tabBuilder: (BuildContext context, int index) {
        return CupertinoTabView(
          builder: (BuildContext context) {
            return switch(index) {
              0 =>  CupertinoPageScaffold(
                      navigationBar: CupertinoNavigationBar(
                        middle: Text('Mapa'),
                      ),
                      child: Center(
                        child: Text('Hello')
                      ),
                    ),
              1 =>  CupertinoPageScaffold(
                      navigationBar: CupertinoNavigationBar(
                        middle: Text('Hledání spojení'),
                      ),
                      child: Center(
                        child: Text('Hello2')
                      ),
                    ),
              _ =>  CupertinoPageScaffold(
                      navigationBar: CupertinoNavigationBar(
                        middle: Text('????????????'),
                      ),
                      child: Center(
                        child: const Text('????????????')
                      ),
                    )
            };
          }
        );
      },
    );
  }
}
