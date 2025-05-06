import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Provider as PaperProvider } from 'react-native-paper';
import { View, TouchableOpacity, StyleSheet } from 'react-native';
import { Text } from 'react-native-paper';

import Dashboard from './screens/Dashboard';
import CampaignManagement from './screens/CampaignManagement';
import Analytics from './screens/Analytics';

const Stack = createStackNavigator();

const Navigation = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="Dashboard"
        screenOptions={{
          headerStyle: {
            backgroundColor: '#5196f4',
          },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}
      >
        <Stack.Screen
          name="Dashboard"
          component={Dashboard}
          options={({ navigation }) => ({
            title: 'Influencer Dashboard',
            headerRight: () => (
              <View style={styles.headerButtons}>
                <TouchableOpacity
                  onPress={() => navigation.navigate('CampaignManagement')}
                  style={styles.headerButton}
                >
                  <Text style={styles.headerButtonText}>Campaigns</Text>
                </TouchableOpacity>
                <TouchableOpacity
                  onPress={() => navigation.navigate('Analytics')}
                  style={styles.headerButton}
                >
                  <Text style={styles.headerButtonText}>Analytics</Text>
                </TouchableOpacity>
              </View>
            ),
          })}
        />
        <Stack.Screen
          name="CampaignManagement"
          component={CampaignManagement}
          options={{ title: 'Campaign Management' }}
        />
        <Stack.Screen
          name="Analytics"
          component={Analytics}
          options={{ title: 'Analytics' }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

const App = () => {
  return (
    <PaperProvider>
      <Navigation />
    </PaperProvider>
  );
};

const styles = StyleSheet.create({
  headerButtons: {
    flexDirection: 'row',
    marginRight: 10,
  },
  headerButton: {
    marginHorizontal: 5,
    padding: 5,
  },
  headerButtonText: {
    color: '#fff',
    fontSize: 16,
  },
});

export default App;