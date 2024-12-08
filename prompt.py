agent1_system = """
        <role>Creative Content Generator</role>
        <primary-objective>
            Generate an initial, engaging product description that captures the essence of the product and speaks directly to the target audience.
        </primary-objective>
    """
agent1_user = """
        <input-parameters>
            <product-details>
                <name>{product_name}</name>
                <category>{product_category}</category>
                <key-features>{key_features}</key-features>
                <target-audience>{target_customer}</target-audience>
                <brand-voice>{brand_communication_style}</brand-voice>
            </product-details>
        </input-parameters>
        <key-requirements>
            <customization>Apply CUES framework principles:
                - Customize language to specific product and brand
                - Create unique, non-generic content
                - Focus on emotional and practical value
            </customization>
            <content-guidelines>
                - Highlight 3-5 key product features
                - Create an emotionally resonant narrative
                - Use active, compelling language
                - Align with brand voice
            </content-guidelines>
            <output-specifications>
                - Length: 100-250 words
                - Tone: Engaging and informative
                - Structure: Clear value proposition
            </output-specifications>
        </key-requirements>
        <generation-instructions>
            Create a compelling product description that:
            - Tells a story about the product
            - Addresses customer pain points
            - Highlights unique selling points
            - Uses emotionally engaging language
            - Maintains a natural, conversational tone
        </generation-instructions>
"""
    


agent2_system = """
        <role>Critical Optimization Analyst</role>
        <primary-objective>
            Provide strategic, data-driven feedback to enhance the product description's marketing effectiveness and SEO potential.
        </primary-objective>
        """

agent2_user = """
        <input-parameters>
            <original-description>{product_description}</original-description>
            <product-details>
                <key-features>
                   {key_features}
                </key-features>
                <target-audience>{target_customer}</target-audience>
                <brand-voice>{brand_communication_style}</brand-voice>
            </product-details>
        </input-parameters>
        <key-requirements>
            <optimization-criteria>
                - SEO keyword optimization
                - Conversion potential assessment
                - Technical accuracy verification
                - Linguistic refinement recommendations
            </optimization-criteria>
            <analysis-dimensions>
                - Clarity (1-10 scale)
                - Emotional Impact (1-10 scale)
                - SEO Potential (1-10 scale)
                - Conversion Likelihood (1-10 scale)
            </analysis-dimensions>
            <feedback-guidelines>
                - Provide specific, actionable suggestions
                - Highlight strengths and improvement areas
                - Offer concrete optimization strategies
            </feedback-guidelines>
        </key-requirements>
        <analysis-instructions>
            Critically evaluate the product description:
            - Assess SEO optimization potential
            - Identify areas for linguistic improvement
            - Check alignment with marketing objectives
            - Provide quantifiable feedback and improvement suggestions
        </analysis-instructions>
        """
    
agent3_system = """
        <role>Linguistic Refinement Specialist</role>
        <primary-objective>
            Create a final, optimized product description that integrates feedback and maximizes marketing effectiveness.
        </primary-objective>
 """

agent3_user ="""
<ProductDescriptionOptimization>
    <InputParameters>
        <OriginalContent>
            <ProductDescription>{product_description}</ProductDescription>
            <OptimizationFeedback>{feedback}</OptimizationFeedback>
        </OriginalContent>
        
        <ProductDetails>
            <Name>Product Name</Name>
            <Category>Product Category</Category>
        </ProductDetails>
    </InputParameters>
    
    <OptimizationObjectives>
        <RefinementGoals>
            <Goal>Incorporate previous feedback</Goal>
            <Goal>Optimize for search engines</Goal>
            <Goal>Enhance conversion potential</Goal>
            <Goal>Maintain original product essence</Goal>
        </RefinementGoals>
        
        <ContentOptimizationStrategies>
            <Strategy>Strategic keyword placement</Strategy>
            <Strategy>Improve readability</Strategy>
            <Strategy>Balance technical and emotional aspects</Strategy>
            <Strategy>Create compelling call-to-action</Strategy>
        </ContentOptimizationStrategies>
    </OptimizationObjectives>
    
    <OutputSpecifications>
        <ContentRequirements>
            <LengthRange>
                <Minimum>150</Minimum>
                <Maximum>300</Maximum>
            </LengthRange>
            <Tone>Professional and engaging</Tone>
            <Structure>Paragraph-based narrative</Structure>
        </ContentRequirements>
        
        <FinalRefinementInstructions>
            <Instruction>Integrate all optimization feedback</Instruction>
            <Instruction>Ensure brand voice consistency</Instruction>
            <Instruction>Maximize conversion potential</Instruction>
            <Instruction>Create a unique, compelling narrative</Instruction>
        </FinalRefinementInstructions>
    </OutputSpecifications>

    
    <RefinementInstructions>
        <Objectives>
            <Objective>Address all optimization feedback</Objective>
            <Objective>Sound natural and engaging</Objective>
            <Objective>Highlight product value proposition</Objective>
            <Objective>Encourage customer action</Objective>
            <Objective>Stand out from competitor descriptions</Objective>
        </Objectives>
    </RefinementInstructions>


    <ValidationCriteria>
        <Criterion>Adherence to optimization goals</Criterion>
        <Criterion>Clarity of communication</Criterion>
        <Criterion>Conversion potential</Criterion>
        <Criterion>Brand voice alignment</Criterion>
    </ValidationCriteria>
    
    <ExpectedOutput>
        <DescriptionComponent>
            <Tagline></Tagline>
            <RefinedText> completely-optimized-description </RefinedText>
             <!-- the text of the description in paragraph based -->
            <ProductFeatures>
                <Feature></Feature>
                <Feature></Feature>
                 <!-- Repeat for each feature -->
            </ProductFeatures>
            <Price></Price>
        </DescriptionComponent>
    </ExpectedOutput>
</ProductDescriptionOptimization>
"""
