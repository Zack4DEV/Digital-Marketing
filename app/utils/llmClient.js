import { Alert } from 'react-native';
import Constants from 'expo-constants';
import * as SecureStore from 'expo-secure-store';

const SYSTEM_MESSAGE = `You Are User Experience Virtual Assistant Agent Over Digital Marketing Platform.
Your task is to guide and answer all users questions in order to improve UX, It has to be clear and concise.
Provide any kind of resources help, suggestions and more navigation facilities over the platform`;

class LLMClient {
  constructor() {
    this.aiPlatform = 'mendable';
    this.workspaceId = Constants.expoConfig.extra?.mendableWorkspaceId;
    this.dataSourceId = Constants.expoConfig.extra?.mendableDataSourceId;
    this.model = Constants.expoConfig.extra?.mendableModel;
  }

  async getApiKey() {
    try {
      return await SecureStore.getItemAsync('mendable_api_key');
    } catch (error) {
      console.error('Error getting API key:', error);
      return null;
    }
  }

  async query(userInput) {
    const apiKey = await this.getApiKey();
    if (!apiKey) {
      Alert.alert('Error', 'API key not configured');
      return null;
    }

    try {
      const response = await fetch('https://api.mendable.ai/v1/completions', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          workspace_id: this.workspaceId,
          data_source_id: this.dataSourceId,
          messages: [
            { role: 'user', content: userInput },
            { role: 'system', content: SYSTEM_MESSAGE }
          ],
          model: this.model,
        }),
      });

      if (!response.ok) {
        throw new Error('API request failed');
      }

      const data = await response.json();
      return data.choices[0]?.message?.content || null;
    } catch (error) {
      console.error('Error querying Mendable:', error);
      Alert.alert('Error', 'Failed to get response from AI');
      return null;
    }
  }
}

export default new LLMClient();